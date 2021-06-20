// Navbar
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

// Language
let i18nListCollapsed = false;

$(".navbar-i18n-btn").click(() => {
  let currentLang =
    window.localStorage.getItem("i18n") || "en-US";
  let i18nListHTML = `
  <div class="close-btn">
      <div class="line"></div>
      <div class="line"></div>
    </div>`;

  i18nLangList.forEach((el) => {
    i18nListHTML += `<li data-lang-code="${
      el.code
    }" class='list-item ${
      el.code === currentLang ? "list-item-active" : ""
    }'>${el.text}</li>`;
  });

  $(".i18n-list").html(i18nListHTML);

  i18nListCollapsed = true;
  $(".i18n-list").addClass("i18n-list-collapsed");
});

// Event delegation
$("body").click(function (e) {
  e = e || window.event;
  let thisNode = e.target || e.srcElement;

  if ($.contains($(".i18n-list")[0], thisNode)) {
    if (
      $(thisNode).attr("class").indexOf("list-item") != -1
    ) {
      let { langCode: targetLang } = thisNode.dataset;
      $("html").attr("lang", targetLang);
      window.localStorage.setItem("i18n", targetLang);

      Object.values($("html .i18n"))
        .slice(0, Object.values($("html .i18n")).length - 2)
        .forEach((el) => {
          handleSwitchLanguage($(el)[0], targetLang);
        });

      i18nListCollapsed = false;
      $(".i18n-list").removeClass("i18n-list-collapsed");
    }

    if (
      $(thisNode).attr("class").indexOf("line") != -1 ||
      $(thisNode).attr("class").indexOf("close-btn") != -1
    ) {
      i18nListCollapsed = false;
      $(".i18n-list").removeClass("i18n-list-collapsed");
    }
  }
});
