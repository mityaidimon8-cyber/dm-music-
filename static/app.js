const tg = window.Telegram?.WebApp;
tg?.ready();
tg?.expand();

const searchInput = document.getElementById("search");
const searchBtn = document.getElementById("searchBtn");
const results = document.getElementById("results");
const navButtons = document.querySelectorAll("nav button");

let favorites = JSON.parse(
  localStorage.getItem("dm_muzic_favorites") || "[]"
);

function renderMessage(message) {
  results.replaceChildren();
  const p = document.createElement("p");
  p.textContent = message;
  results.appendChild(p);
}

searchBtn.addEventListener("click", () => {
  const query = searchInput.value.trim();

  if (!query) {
    renderMessage("Введи название песни или исполнителя.");
    return;
  }

  renderMessage(
    `Поиск «${query}». Подключение к VK Music ещё не настроено.`
  );
});

searchInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") searchBtn.click();
});

navButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const tab = button.dataset.tab;

    if (tab === "music") {
      renderMessage(
        favorites.length
          ? `Избранное: ${favorites.length} трек(ов).`
          : "Пока нет избранных треков."
      );
    } else if (tab === "search") {
      searchInput.focus();
      renderMessage("Введи название песни или исполнителя.");
    } else if (tab === "playlists") {
      renderMessage("Создание плейлистов добавим следующим этапом.");
    } else if (tab === "settings") {
      renderMessage(
        "DM Muzic · Настройки плавных переходов и воспроизведения появятся после подключения плеера."
      );
    }

    navButtons.forEach((item) => {
      item.setAttribute("aria-pressed", String(item === button));
    });
  });
});

renderMessage("DM Muzic готов. Для поиска реальных треков подключим VK.");
