// 화면 동작 코드 — 백엔드 API를 호출하고, 받은 결과를 화면에 그린다

const API = window.API_BASE_URL;   // config.js에서 정한 백엔드 주소
let currentConversationId = null;  // 지금 보고 있는 대화의 id (새 대화면 null)

// ── 공통 도구 ─────────────────────────────────────────────

const byId = (id) => document.getElementById(id);  // id로 화면 요소를 찾는 짧은 이름

// 백엔드 API 호출 공통 함수: 성공하면 응답 JSON을 JS 객체로 돌려주고, 실패하면 에러를 던진다
async function api(path, options = {}) {
  const res = await fetch(API + path, {
    ...options,
    headers: options.body ? { "Content-Type": "application/json" } : undefined,  // 보낼 데이터가 있을 때만 JSON이라고 알림
  });
  if (!res.ok) throw new Error(`API 오류 ${res.status}`);  // 200번대가 아니면 실패로 처리
  return res.json();
}

// 사용자·AI가 쓴 글자를 HTML 태그로 해석하지 않게 바꿔 줌 (화면 깨짐·스크립트 삽입 방지)
function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

// ── 서버 깨우기 + 데이터 요약 ─────────────────────────────

// 콜드스타트 대응: 헬스체크(GET /)가 응답할 때까지 안내 띠를 보여주고, 응답이 오면 숨김
async function wakeServer() {
  const banner = byId("server-status");
  try {
    await api("/");                  // 잠든 무료 서버라면 여기서 최대 1분 가까이 기다림
    banner.classList.add("hidden");
  } catch (e) {
    banner.textContent = "서버에 연결하지 못했어요. 잠시 후 새로고침해 주세요.";
  }
}

// 데이터 요약(GET /api/data/summary)을 요약 칸에 표시 — AI가 답변할 때 쓰는 것과 같은 요약
async function loadSummary() {
  const box = byId("summary");
  const s = await api("/api/data/summary");
  if (s.count === 0) {
    box.textContent = "저장된 데이터가 없습니다.";
    return;
  }
  box.innerHTML =
    `📊 <b>기간</b> ${escapeHtml(s.period)} · <b>개수</b> ${s.count}개 · ` +
    `<b>평균</b> ${s.metrics.average}원 · <b>최고</b> ${s.metrics.max}원 · ` +
    `<b>최저</b> ${s.metrics.min}원 · <b>추세</b> ${escapeHtml(s.trend)}`;
}

// ── 채팅 ─────────────────────────────────────────────────

// 말풍선 하나를 대화창에 추가 (AI 답변의 **굵게** 표시만 간단히 살림)
function addMessage(role, content) {
  const box = byId("messages");
  const div = document.createElement("div");
  div.className = `msg ${role}`;  // "msg user" 또는 "msg assistant" → CSS가 위치·색을 정함
  div.innerHTML = escapeHtml(content).replace(/\*\*(.+?)\*\*/g, "<b>$1</b>");
  box.appendChild(div);
  box.scrollTop = box.scrollHeight;  // 새 말풍선이 보이도록 맨 아래로 스크롤
}

// 로딩 중에는 로딩 문구를 보이고 입력·전송 버튼을 막아 중복 전송을 방지
function setLoading(on) {
  byId("loading").classList.toggle("hidden", !on);
  byId("chat-input").disabled = on;
  byId("chat-form").querySelector("button").disabled = on;
}

// 채팅 전송: 내 말풍선 → 로딩 표시 → POST /api/chat → AI 답변 말풍선 → 대화 목록 새로고침
async function sendChat(event) {
  event.preventDefault();  // 폼 전송 시 페이지가 새로고침되는 기본 동작 막기
  const input = byId("chat-input");
  const message = input.value.trim();
  if (!message) return;    // 공백만 입력하면 무시

  addMessage("user", message);
  input.value = "";
  setLoading(true);
  try {
    const data = await api("/api/chat", {
      method: "POST",
      body: JSON.stringify({ message, conversation_id: currentConversationId }),  // 이어지는 대화면 id를 함께 보냄
    });
    currentConversationId = data.conversation_id;  // 새 대화였다면 서버가 만든 id를 기억 → 다음 질문은 같은 대화에 저장
    addMessage("assistant", data.reply);
    loadConversations();
  } catch (e) {
    addMessage("assistant", `⚠️ 답변을 받지 못했어요. 잠시 후 다시 시도해 주세요. (${e.message})`);
  } finally {
    setLoading(false);  // 성공이든 실패든 로딩 표시는 끔
    byId("chat-input").focus();
  }
}

// ── 대화 기록 ────────────────────────────────────────────

// 대화 목록(GET /api/conversations)을 최신순으로 표시 — 목록 API는 메시지 대신 개수만 줌
async function loadConversations() {
  const list = byId("conversation-list");
  const convs = await api("/api/conversations");
  convs.sort((a, b) => (b.created_at || "").localeCompare(a.created_at || ""));  // 최신 대화가 위로
  list.innerHTML = "";
  if (convs.length === 0) {
    list.innerHTML = `<li class="empty">저장된 대화가 없습니다</li>`;
    return;
  }
  for (const c of convs) {
    const li = document.createElement("li");
    if (c.id === currentConversationId) li.className = "active";  // 지금 보고 있는 대화 강조
    const when = new Date(c.created_at).toLocaleString("ko-KR", {
      month: "numeric", day: "numeric", hour: "2-digit", minute: "2-digit",  // 예: 10. 23. 오전 11:26
    });
    li.innerHTML =
      `<span class="conv-title">${escapeHtml(c.title)}</span>` +
      `<small>${when} · 💬 ${c.message_count}</small>`;
    li.onclick = () => openConversation(c.id);  // 클릭하면 그 대화 불러오기

    const del = document.createElement("button");
    del.className = "conv-del";
    del.title = "대화 삭제";
    del.textContent = "×";
    del.onclick = (e) => {
      e.stopPropagation();  // 삭제 버튼 클릭이 '불러오기' 클릭으로 번지지 않게 막음
      deleteConversation(c.id);
    };
    li.appendChild(del);
    list.appendChild(li);
  }
}

// 특정 대화 불러오기(GET /api/conversations/{id}) → 저장된 메시지를 대화창에 다시 표시
async function openConversation(id) {
  try {
    const conv = await api(`/api/conversations/${id}`);
    currentConversationId = id;  // 이후 질문은 이 대화에 이어서 저장됨
    byId("messages").innerHTML = "";
    conv.messages.forEach((m) => addMessage(m.role, m.content));
    loadConversations();         // 강조 표시 갱신
  } catch (e) {
    alert(`대화를 불러오지 못했어요. (${e.message})`);
  }
}

// 대화 삭제(DELETE /api/conversations/{id})
async function deleteConversation(id) {
  if (!confirm("이 대화를 삭제할까요?")) return;
  try {
    await api(`/api/conversations/${id}`, { method: "DELETE" });
    if (id === currentConversationId) startNewChat();  // 보고 있던 대화를 지웠으면 화면도 비움
    else loadConversations();
  } catch (e) {
    alert(`대화를 삭제하지 못했어요. (${e.message})`);
  }
}

// 새 대화: 대화 id를 비우고 대화창 초기화 → 다음 질문은 새 대화로 저장됨
function startNewChat() {
  currentConversationId = null;
  byId("messages").innerHTML = "";
  loadConversations();
  byId("chat-input").focus();
}

// ── 데이터 관리 (CRUD) ───────────────────────────────────

// 저장/수정/삭제 결과를 데이터 관리 칸에 표시
function showStatus(text, isError = false) {
  const p = byId("data-status");
  p.textContent = text;
  p.className = isError ? "status error" : "status";
}

// 데이터 목록(GET /api/data)을 날짜 최신순 표로 표시
async function loadData() {
  const rows = await api("/api/data");
  rows.sort((a, b) => b.date.localeCompare(a.date));
  const tbody = byId("data-list");
  tbody.innerHTML = "";
  for (const r of rows) {
    const tr = document.createElement("tr");
    tr.innerHTML =
      `<td>${escapeHtml(r.date)}</td><td>${r.value}</td><td>${escapeHtml(r.memo || "")}</td>` +
      `<td><button class="edit">수정</button> <button class="del">삭제</button></td>`;
    tr.querySelector(".edit").onclick = () => editData(r);
    tr.querySelector(".del").onclick = () => deleteData(r);
    tbody.appendChild(tr);
  }
  byId("data-count").textContent = `(${rows.length}개)`;
}

// 데이터가 바뀌면 목록과 요약을 함께 새로고침 — 요약은 AI 답변의 근거라 같이 갱신해야 함
async function refreshData() {
  await Promise.all([loadData(), loadSummary()]);
}

// 데이터 추가(POST /api/data)
async function addData(event) {
  event.preventDefault();
  const item = {
    date: byId("data-date").value,
    value: Number(byId("data-value").value),  // 입력칸 값(문자열) → 숫자 (백엔드 Pydantic이 float을 요구)
    memo: byId("data-memo").value.trim(),
  };
  try {
    const saved = await api("/api/data", { method: "POST", body: JSON.stringify(item) });
    showStatus(`✅ 저장되었습니다: ${saved.date} / ${saved.value}`);
    byId("data-form").reset();
    await refreshData();
  } catch (e) {
    showStatus(`❌ 저장 실패 (${e.message})`, true);
  }
}

// 데이터 수정(PUT /api/data/{id}): 새 값과 메모를 입력받아 덮어씀
async function editData(r) {
  const value = prompt(`${r.date}의 새 값을 입력하세요`, r.value);
  if (value === null) return;  // 취소
  if (value.trim() === "" || isNaN(Number(value))) {
    showStatus("❌ 값은 숫자로 입력해야 합니다", true);
    return;
  }
  const memo = prompt("메모를 입력하세요 (비워도 됨)", r.memo || "");
  if (memo === null) return;   // 취소
  try {
    await api(`/api/data/${r.id}`, {
      method: "PUT",
      body: JSON.stringify({ date: r.date, value: Number(value), memo: memo.trim() }),
    });
    showStatus(`✅ 수정되었습니다: ${r.date} → ${Number(value)}`);
    await refreshData();
  } catch (e) {
    showStatus(`❌ 수정 실패 (${e.message})`, true);
  }
}

// 데이터 삭제(DELETE /api/data/{id})
async function deleteData(r) {
  if (!confirm(`${r.date} 데이터를 삭제할까요?`)) return;
  try {
    await api(`/api/data/${r.id}`, { method: "DELETE" });
    showStatus(`✅ 삭제되었습니다: ${r.date}`);
    await refreshData();
  } catch (e) {
    showStatus(`❌ 삭제 실패 (${e.message})`, true);
  }
}

// ── 시작 ─────────────────────────────────────────────────

// 버튼·폼에 동작 연결 → 서버 깨우기 → 요약·대화 목록·데이터 목록을 한꺼번에 불러오기
async function init() {
  byId("chat-form").addEventListener("submit", sendChat);
  byId("new-chat-btn").addEventListener("click", startNewChat);
  byId("data-form").addEventListener("submit", addData);

  await wakeServer();
  try {
    await Promise.all([loadSummary(), loadConversations(), loadData()]);
  } catch (e) {
    byId("summary").textContent = `데이터를 불러오지 못했어요. 새로고침해 주세요. (${e.message})`;
  }
}

init();
