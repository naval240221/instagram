function showFollowingModal(uname) {
    // send AJAX request to get list of followings
    $.ajax({
        url: '/followings/' + uname,
        success: function (response) {
            // display list of followings in a modal
            var modalBody = $('#followingModal .modal-body');
            modalBody.empty();
            var htmlString = $('<div class="card border-0"><div class="card-body"><ul class="list-group list-group-flush">')
            modalBody.append(htmlString)
            for (var i = 0; i < response.length; i++) {
                var following = response[i];
                var followingItem = $('<li class="list-group-item d-flex align-items-center justify-content-between border-0"></li>');
                var followingDiv = $('<div class="d-flex align-items-center"></div>')
                // var followingLink = $('<a href="' + following.profile_url + '"></a>');
                var followingImg = $('<img src="' + following.profile_image_url + '" alt="' + following.username + '" class="rounded-circle" style="width: 50px; height: 50px;">');
                var followingLink = $('<a href="/profile/' + following.username + '" class="ms-3">' + following.username + '</a>');
                followingDiv.append(followingImg).append(followingLink)
                var unfollowBtn = $('<a class="btn btn-sm btn-primary" href="/unfollow/' + following.username + '">Unfollow</a>"');
                followingItem.append(followingDiv).append(unfollowBtn);
                modalBody.append(followingItem);
            }
            modalBody.append($('</ul></div></div>'))
            $('#followingModal').modal('show');
        }
    });
}

function showFollowersModal(uname) {
    // send AJAX request to get list of followings
    $.ajax({
        url: '/followers/' + uname,
        success: function (response) {
            // display list of followings in a modal
            var modalBody = $('#followerModal .modal-body');
            modalBody.empty();
            var htmlString = $('<div class="card border-0"><div class="card-body"><ul class="list-group list-group-flush">')
            modalBody.append(htmlString)
            for (var i = 0; i < response.length; i++) {
                var following = response[i];
                var followingItem = $('<li class="list-group-item d-flex align-items-center justify-content-between border-0"></li>');
                var followingDiv = $('<div class="d-flex align-items-center"></div>')
                // var followingLink = $('<a href="' + following.profile_url + '"></a>');
                var followingImg = $('<img src="' + following.profile_image_url + '" alt="' + following.username + '" class="rounded-circle" style="width: 50px; height: 50px;">');
                var followingLink = $('<a href="/profile/' + following.username + '" class="ms-3">' + following.username + '</a>');
                followingDiv.append(followingImg).append(followingLink)
                // var unfollowBtn = $('<a class="btn btn-sm btn-primary" href="/unfollow/' + following.username + '">Unfollow</a>"');
                followingItem.append(followingDiv)
                modalBody.append(followingItem);
            }
            modalBody.append($('</ul></div></div>'))
            $('#followerModal').modal('show');
        }
    });
}