/ Function to send a swap request
function sendSwapRequest(fromUser , toUser , skillOffered, skillRequested) {
    fetch('/request_swap', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            from_user: fromUser ,
            to_user: toUser ,
            skill_offered: skillOffered,
            skill_requested: skillRequested
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        location.reload(); // Reload the page to see updated requests
    })
    .catch(error => console.error('Error:', error));
}

// Function to respond to a swap request
function respondSwap(fromUser , action) {
    fetch('/respond_swap', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            from_user: fromUser ,
            action: action
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        location.reload(); // Reload the page to see updated requests
    })
    .catch(error => console.error('Error:', error));
}

// Function to search for users by skill
function searchUsers() {
    const skill = document.getElementById('skillSearch').value;
    fetch(`/users?skill=${skill}`)
        .then(response => response.json())
        .then(data => {
            // Update the user list on the page
            const userList = document.getElementById('userList');
            userList.innerHTML = ''; // Clear existing list
            data.forEach(user => {
                const li = document.createElement('li');
                li.textContent = `${user.name} - Skills Offered: ${user.skills_offered.join(', ')}`;
                userList.appendChild(li);
            });
        })
        .catch(error => console.error('Error:', error));
}

// Event listener for search input
document.getElementById('skillSearchButton').addEventListener('click', searchUsers);
