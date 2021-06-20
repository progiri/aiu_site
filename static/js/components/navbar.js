let navbarCollapsed = false;

$(".navbar-collpase-btn").click(() => {
  navbarCollapsed = !navbarCollapsed;

  if (navbarCollapsed) {
    $(".navbar-sidebar").addClass(
      "navbar-sidebar-collapsed"
    );
  } else {
    $(".navbar-sidebar").removeClass(
      "navbar-sidebar-collapsed"
    );
  }
});
