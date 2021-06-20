const i18nLangList = [
  { text: "ENG", code: "en-US" },
  { text: "Рус", code: "ru-RU" },
  { text: "Қаз", code: "kk-KZ" },
  { text: "中", code: "zh-CN" },
];

function handleSwitchLanguage(node, currentLang) {
  let { i18nId } = node.dataset;

  switch (currentLang) {
    case "en-US":
      $(node).text(i18nENGLISH[i18nId]);
      break;
    case "ru-RU":
      $(node).text(i18nRUSSIAN[i18nId]);
      break;
    case "kk-KZ":
      $(node).text(i18nKAZAH[i18nId]);
      break;
    case "zh-CN":
      $(node).text(i18nCHINESE[i18nId]);
      break;
    default:
      $(node).text(i18nENGLISH[i18nId]);
  }
}

$(function () {
  let targetLang =
    window.localStorage.getItem("i18n") || "en-US";

  Object.values($("html .i18n"))
    .slice(0, Object.values($("html .i18n")).length - 2)
    .forEach((el) => {
      handleSwitchLanguage($(el)[0], targetLang);
    });
});

const i18nENGLISH = {
  "lang": "ENG",
  "home": "Home",
  "news": "News",
  "engineering": "Engineering",
  "read more": "Read More",
};

const i18nRUSSIAN = {
  "lang": "Рус",
  "home": "Глвный",
  "news": "Новости",
  "engineering": "Инженерное дело",
  "read more": "Читать далее",
};

const i18nKAZAH = {
  "lang": "Қаз",
  "home": "Негізгі",
  "news": "Жаңалық",
  "engineering": "Инженерлік",
  "read more": "Жалғасты оқу",
};

const i18nCHINESE = {
  "lang": "中",
  "home": "主页",
  "news": "新闻",
  "engineering": "工程",
  "read more": "查看更多",
};
