const ratingToStars = (rating) => {
  if (!rating || rating > 5) {
    return `${"<i class='bi bi-star'></i>".repeat(5)}`;
  }
  let fullStars = parseInt(rating);
  let halfStar = rating - fullStars >= 0.5 ? 1 : 0;
  let emptyStars = 5 - fullStars - halfStar;
  let stars = `${"<i class='bi bi-star-fill'></i>".repeat(fullStars)}${"<i class='bi bi-star-half'></i>".repeat(halfStar)}${"<i class='bi bi-star'></i>".repeat(emptyStars)}`;
  return stars;
};

const createStars = () => {
  starRatings = document.querySelectorAll(".star-rating.no-stars");
  if (starRatings.length > 0) {
    for (let i = 0; i < starRatings.length; i++) {
      starRatings[i].innerHTML = ratingToStars(starRatings[i].textContent);
      starRatings[i].classList.remove("no-stars");
    }
  }
};
createStars();

function viewProgram(id) {
  window.location.href = `/programs/program/${id}/`;
}
function viewDashboard() {
  window.location.href = `/user/dashboard/`;
}
function getCSRFToken() {
  const cookieValue = document.cookie.match(
    "(^|;)\\s*" + "csrftoken" + "\\s*=\\s*([^;]+)",
  );
  return cookieValue ? cookieValue.pop() : "";
}

function userProgramCreateDelete(programId, method, contId) {
  fetch("/programs/program-cd/", {
    method: method,
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRFToken(), // Include the CSRF token in the headers
    },
    body: JSON.stringify({ program_id: programId }),
  })
    .then((response) => response.json())
    .then((data) => {
      let message = data.message;
      if (data.category == "success") {
        triggerToast(message, "success");
        if (method == "DELETE") {
          removeListItem(contId);
        }
      } else {
        triggerToast(message, "danger");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function triggerToast(message, category) {
  const toastLive = document.getElementById("liveToast");
  let toastBody = toastLive.querySelector(".toast-body");
  toastBody.textContent = message;
  toastLive.className = `toast bg-${category}`;
  const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLive);
  toastBootstrap.show();
}
