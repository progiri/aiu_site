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

let i18nListCollapsed = false;

$(".navbar-i18n-btn").click(() => {
  i18nListCollapsed = true;
  $(".i18n-list").addClass("i18n-list-collapsed");
});

$(".i18n-list .close-btn").click(() => {
  i18nListCollapsed = false;
  $(".i18n-list").removeClass("i18n-list-collapsed");
});

$(".i18n-list .list-item").click(function () {
  console.log(this.dataset.langCode);
});
