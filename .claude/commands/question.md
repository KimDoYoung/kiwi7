---
description: 질문에 답변하고 docs/questions.md에 기록한다.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
argument-hint: <질문 내용>
---

# 개요

사용자의 질문에 답변하고, 질문과 답변 내용을 `docs/questions.md` 파일에 추가한다.

## 작업 흐름

### 1. 질문 확인

- 사용자가 입력한 질문 내용: `$ARGUMENTS`

### 2. 답변 작성

1. 질문 내용을 분석하고 적절한 답변을 작성한다.
2. 필요시 코드베이스를 탐색하거나 웹 검색을 수행한다.
3. 답변은 명확하고 간결하게 작성한다.

### 3. 문서에 기록

1. `docs/questions.md` 파일이 없으면 새로 생성한다.
2. 파일 끝에 다음 형식으로 추가한다:

```markdown
## [날짜] 질문 제목

**Q:** 질문 내용

**A:** 답변 내용
```

3. 날짜 형식: `YYYY-MM-DD`

### 4. 완료 보고

- 사용자에게 답변을 보여주고, 문서에 기록되었음을 알린다.
