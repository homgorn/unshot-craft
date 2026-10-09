# TypeSafe (typesafe-ai) — дип-рисерч, польза и инструкция

**Дата исследования:** 2026-10-09 · **Статус в репо:** установлен project-local
(`.agents/skills/typesafe-ai`, `skills-lock.json`) · **Правило:** ADR-0008
(суждения — только advisory, никогда гейты).

## 0. Вывод в один абзац

TypeSafe — API «System One»-моделей (флагман Jev): вместо генерации текста —
типизированные суждения с вероятностями (Choice / Noul / Score), которые код
комбинирует. Для shotcraft это дешёвый советчик по пяти задачам (проверка
цитат, качество переводов, реранк поиска, подбор скиллов, guardrails), но не
гейт: вероятности не детерминированы, а наши гейты обязаны быть
детерминированными. Скилл MIT, установлен, ключ — только в `.env`
(`TYPESAFE_API_KEY`), в репо — лишь имя. Уверенность в выводе 9/10.

## 1. Что это такое (reported, первоисточники, 2026-10-09)

- **Модель:** System One — решения внутри софта, не чат. Обучение RLCD
  (Reinforcement Learning for Calibrated Decisions), не RLHF. Флагман Jev,
  алиас `jev-latest` (в примерах доков отвечает `jev-1.13.0`).
  Источник: `https://typesafe.ai/` (homepage), `https://docs.typesafe.ai/llms.txt`.
  Уверенность 10/10.
- **Контракт:** `POST https://api.typesafe.ai/v1/systemone`,
  `Authorization: Bearer <API_KEY>`, тело `{state, model, questions}`; ответ —
  `{answers: {<id>: {choice|noul|score, probabilities, confidence}}, usage:
  {input_tokens, output_tokens}}`. Три примитива: **Choice** (один из набора +
  распределение), **Noul** (вероятность «да», без отдельной confidence),
  **Score** (позиция на упорядоченных уровнях).
  Источник: `https://docs.typesafe.ai/introduction/quickstart.md`. 10/10.
- **SDK:** Python `typesafe-sdk` (`pip install typesafe-sdk`, Python ≥ 3.10,
  sync `TypeSafeClient` + async `AsyncTypeSafeClient`, читает `TYPESAFE_API_KEY`
  из окружения); JavaScript SDK. Консоль и Playground: `console.typesafe.ai`.
  Источник: `https://docs.typesafe.ai/sdk/python.md`. 10/10.
- **Скилл:** репозиторий `typesafe-ai/skills`, файл `skills/typesafe-ai/`
  (только `SKILL.md` + `LICENSE`, проверено через GitHub API 2026-10-09),
  лицензия MIT (заявлена в README репо; сам текст LICENSE сверен в установке).
  Установка: Claude Code plugin (`marketplace add` + `install`) либо
  `npx skills add typesafe-ai/skills --skill typesafe-ai` (project-local по
  умолчанию, `-g` — глобально), либо ручная копия каталога. Обновления — тем же
  методом (`plugin update` / `npx skills update` / замена каталога).
  Источник: `https://docs.typesafe.ai/agent-skill.md`. 10/10.
- **Живые доки — источник истины.** Скилл требует читать `docs.typesafe.ai` под
  задачу (индекс `llms.txt`, страницы как `.md`). Версионные детали из памяти
  не брать. 10/10.
- **Деньги (reported, заявление вендора):** homepage claims `$42` за миллиард
  input-токенов и «193.6x faster / 444.6x cheaper» против LLM-пайплайна на их
  бенче — вендорский замер, не воспроизведён нами. Статус Jev — early access
  (homepage, 2026-10-09). Публичного прайсинга постранично в доках нет —
  смотреть `console.typesafe.ai`. Уверенность в цифрах 6/10 (их методика), в
  факте «дешевле LLM на порядки» 8/10.
- **Legal/ToS (reported):** DPA, Master Customer Agreement, Privacy Policy
  (обязательство не тренироваться на данных пользователей), ZDR — только
  enterprise (`sales@typesafe.ai`). Источник:
  `https://docs.typesafe.ai/legal.md`. 9/10. Наш корпус — публичный (upstream
  Apache-2.0 + MIT-каталог), секретов в state не отправлять до Chase-режима;
  см. ADR-0008.

## 2. Как это установлено у нас (measured)

```powershell
npx -y skills add typesafe-ai/skills --skill typesafe-ai -y
```

- Агент `opencode` детектирован автоматически, установка неинтерактивная.
- Security-скан установщика: Safe, 0 Socket-алертов, Snyk Low Risk (2026-10-09).
- В репо: `.agents/skills/typesafe-ai/SKILL.md` + `LICENSE` (копия апстрима,
  руками не править — обновления затирают), `skills-lock.json` (пин
  `sourceType: github`, `computedHash`).
- Проверка: скилл загружается штатным вызовом по id `typesafe-ai` (2026-10-09).
  Уверенность 10/10.

## 3. Польза для shotcraft (inferred, привязка к нашим гейтам)

| # | Задача | Паттерн/кукбук | Почему нам |
|---|---|---|---|
| 1 | Проверка цитат вики против источников | `citation_check` (Choice: поддерживает ли контекст claim) | Усиливает `docs_freshness.py`: машина находит кандидатов на новые CLAIMS |
| 2 | Качество переводов `ru/es/de/fr/pt/ko/ja` | Score (fluency/adequacy) + Noul «остался CJK?» | Подсветка для `translate.py report`; порог — человек, не гейт |
| 3 | Реранк FTS-поиска | `rerank_typesafe` (их замер: top-1 5%→18%) | `query.py search` и `/cards?q=` поверх каскада unicode61→trigram→LIKE |
| 4 | Подбор скиллов под задачу (260+ штук) | `skill_suggestion` (ранжирование каталога) | Наш кейс один в один: `skill-fit` + TypeSafe-ранжир |
| 5 | Guardrails для будущих LLM-шагов | `llm_guardrails` | Скрининг входов/выходов, когда появятся модельные шаги |

Жёсткое ограничение (ADR-0008): всё выше — **advisory**. Гейт, зависящий от
вероятности, — это гейт, который иногда пропускает брак и иногда валит зелёное.
TypeSafe готовит данные для человека/верификатора, решения принимают код и люди.

## 4. Как использовать (инструкция себе и агентам)

1. Триггер: «нужно программируемое здравомыслие», «заменить хрупкий парсинг
   суждением», брейншторм AI-возможностей, `prompt-and-parse` → структура.
   Загрузка: вызовом скилла `typesafe-ai`, дальше — по его тексту.
2. Перед интеграцией прочитать живую страницу SDK/примитива под задачу
   (топ-5 стартовых: `concepts/system-one.md`, `concepts/use-case-map.md`,
   `primitives.md`, `confidence.md`, `sdk/python.md`).
3. Вопросы и пороги — в одном файле констант, ревьюить глазами (принцип №3
   «good vibe coding principles» из `agent-skill.md`). Пороги калибровать на
   наших данных, cookbook-числа — примеры, не нормы.
4. Нужен ключ: `TYPESAFE_API_KEY` в `.env` (в репо только имя, см.
   `.env.example`). Без ключа — Playground и чтение доков.
5. Промпты-стартеры (из `agent-skill.md`):
   - «Using the TypeSafe skill, explore the project and find opportunities for
     using intelligent judgement to stand in for complex parsing or other
     fragile code.»
   - «Using the TypeSafe skill, run some experiments using the TypeSafe API key
     that I've exported to `TYPESAFE_API_KEY`. Propose changes based on the most
     promising results.»
   - «Using the TypeSafe skill, analyze my code and see if there are any
     applicable cookbooks that show how I could refactor my code to be less
     fragile or complex.»

## 5. Инструкция владельцу (что сделать руками)

1. Ключ: `console.typesafe.ai/keys` → создать → в локальный `.env`
   (`copy .env.example .env`, раскомментировать `TYPESAFE_API_KEY=`).
   Никому не отправлять, в чат не вставлять — см. правило секретов в AGENTS.md.
2. В Claude Code (если понадобится там): две команды из `agent-skill.md`;
   здесь, в opencode/OpenChamber, уже стоит project-local — ничего не делать.
3. Обновления: `npx skills update` (или `npx -y skills update -p`) время от
   времени; `skills-lock.json` закоммичен — diff хеша покажет, что приехало.
4. Первая задача-кандидат (дешёвая, без ключа — чтение): «прочеши `wiki/`
   кукбуком citation_check и предложи 10 кандидатов в CLAIMS для
   `docs_freshness.py`». С ключом — прогнать Score по `site/locales/ru/ui.json`.

## 6. Конфликты, гэпы, журнал запросов

- **Конфликт:** «193.6x/444.6x» и «$42» — маркетинг вендора на их задаче; наши
  пороги и бюджеты мерить самим (скилл того же требует). Побеждает измерение.
- **Гэп:** точный биллинг/лимиты/рейты — только консоль (нужен аккаунт);
  проверялось: homepage, llms.txt, quickstart, python SDK, agent-skill, legal —
  прайс-страницы там нет.
- **Гэп:** субагенты в этой среде без сети (`ENOTFOUND openrouter.ai`) —
  рисерч вёлся главной сессией через прямые fetch.
- **Почему не в БД/вики:** `platform/db/shotcraft.db` и `wiki/` —Generated
  (AGENTS.md правила 2–3): БД строится ингестом из корпусов, вики — из БД.
  Скилл — инструмент, не данные корпуса; его место — `.agents/skills/` +
  этот документ + ADR-0008. Ручная правка вики под это была бы багом.
- **Запросы (все 2026-10-09, все primary):**

```text
2026-10-09  fetch raw.githubusercontent.com/.../skills/typesafe-ai/SKILL.md  200
2026-10-09  fetch raw.githubusercontent.com/.../skills/main/README.md        200
2026-10-09  fetch docs.typesafe.ai/llms.txt                                 200
2026-10-09  fetch docs.typesafe.ai/agent-skill.md                           200
2026-10-09  fetch docs.typesafe.ai/sdk/python.md                            200
2026-10-09  fetch docs.typesafe.ai/introduction/quickstart.md               200
2026-10-09  fetch typesafe.ai/                                              200
2026-10-09  fetch docs.typesafe.ai/legal.md                                 200
2026-10-09  fetch api.github.com/repos/typesafe-ai/skills/contents/...      200
2026-10-09  npx skills add typesafe-ai/skills --skill typesafe-ai -y        ok (Safe/0 alerts/Low Risk)
```
