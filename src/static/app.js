document.addEventListener("DOMContentLoaded", () => {
  const activitiesList = document.getElementById("activities-list");
  const activitySelect = document.getElementById("activity");
  const signupForm = document.getElementById("signup-form");
  const messageDiv = document.getElementById("message");

  // Function to fetch activities from API
  async function fetchActivities() {
    try {
      const response = await fetch("/activities");
      const activities = await response.json();

      // Clear loading message
      activitiesList.innerHTML = "";

      // Populate activities list
      Object.entries(activities).forEach(([name, details]) => {
        const activityCard = document.createElement("div");
        activityCard.className = "activity-card";

        const spotsLeft = details.max_participants - details.participants.length;

        activityCard.innerHTML = `
          <div class="activity-header">
            <h4>${name}</h4>
            <span class="badge">${details.participants.length} participants</span>
          </div>
          <p>${details.description}</p>
          <p><strong>Schedule:</strong> ${details.schedule}</p>
          <p><strong>Availability:</strong> ${spotsLeft} spots left</p>
          <div class="participants">
            <h5>Participants</h5>
            <!-- participants list will be populated here -->
          </div>
        `;

        // Populate participants list safely (use DOM methods to avoid injection)
        const participantsContainer = activityCard.querySelector(".participants");
        if (details.participants && details.participants.length > 0) {
          const ul = document.createElement("ul");
          ul.className = "participants-list no-bullets";
          details.participants.forEach((p) => {
            const li = document.createElement("li");
            li.className = "participant-item";
            // Create participant name span
            const nameSpan = document.createElement("span");
            nameSpan.textContent = p;
            // Create delete icon
            const deleteBtn = document.createElement("span");
            deleteBtn.className = "delete-icon";
            deleteBtn.title = "Remove participant";
            deleteBtn.innerHTML = "&#128465;"; // Unicode trash can
            deleteBtn.style.cursor = "pointer";
            deleteBtn.style.marginLeft = "8px";
            deleteBtn.onclick = async () => {
              await unregisterParticipant(name, p);
            };
            li.appendChild(nameSpan);
            li.appendChild(deleteBtn);
            ul.appendChild(li);
          });
          participantsContainer.appendChild(ul);
        } else {
          const empty = document.createElement("p");
          empty.className = "participants-empty";
          empty.textContent = "No participants yet";
          participantsContainer.appendChild(empty);
        }
  // Unregister participant function
  async function unregisterParticipant(activity, participant) {
    try {
      const response = await fetch(`/activities/${encodeURIComponent(activity)}/unregister?email=${encodeURIComponent(participant)}`, {
        method: "POST"
      });
      const result = await response.json();
      if (response.ok) {
        messageDiv.textContent = result.message || "Participant removed.";
        messageDiv.className = "success";
        fetchActivities();
      } else {
        messageDiv.textContent = result.detail || "Failed to remove participant.";
        messageDiv.className = "error";
      }
      messageDiv.classList.remove("hidden");
      setTimeout(() => {
        messageDiv.classList.add("hidden");
      }, 3000);
    } catch (error) {
      messageDiv.textContent = "Error removing participant.";
      messageDiv.className = "error";
      messageDiv.classList.remove("hidden");
    }
  }

        activitiesList.appendChild(activityCard);

        // Add option to select dropdown
        const option = document.createElement("option");
        option.value = name;
        option.textContent = name;
        activitySelect.appendChild(option);
      });
    } catch (error) {
      activitiesList.innerHTML = "<p>Failed to load activities. Please try again later.</p>";
      console.error("Error fetching activities:", error);
    }
  }

  // Handle form submission
  signupForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const activity = document.getElementById("activity").value;

    try {
      const response = await fetch(
        `/activities/${encodeURIComponent(activity)}/signup?email=${encodeURIComponent(email)}`,
        {
          method: "POST",
        }
      );

      const result = await response.json();

      if (response.ok) {
        messageDiv.textContent = result.message;
        messageDiv.className = "success";
        signupForm.reset();
      } else {
        messageDiv.textContent = result.detail || "An error occurred";
        messageDiv.className = "error";
      }

      messageDiv.classList.remove("hidden");

      // Hide message after 5 seconds
      setTimeout(() => {
        messageDiv.classList.add("hidden");
      }, 5000);
    } catch (error) {
      messageDiv.textContent = "Failed to sign up. Please try again.";
      messageDiv.className = "error";
      messageDiv.classList.remove("hidden");
      console.error("Error signing up:", error);
    }
  });

  // Initialize app
  fetchActivities();
});
