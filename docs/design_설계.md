# CSS 설계 분석 및 개선 제안

## 1. 현재 설계 분석 (Current Status)

### 1.1 기술 스택
- **Framework**: Tailwind CSS (via CDN), DaisyUI (via CDN)
- **Icons**: Bootstrap Icons (via CDN)
- **Script**: Alpine.js (via CDN)
- **Custom CSS**: `public/css/style.css` (매우 적음, 주로 유틸리티 클래스 사용)

### 1.2 코드 구조 특징
- **HTML 중심의 스타일링**: 별도의 CSS 파일 작성보다는 HTML 태그 내에 Tailwind 유틸리티 클래스(`w-full`, `text-center`, `p-4` 등)를 직접 사용하여 스타일을 정의하고 있습니다.
- **DaisyUI 컴포넌트 활용**: `btn`, `card`, `navbar`, `badge` 등 DaisyUI의 미리 정의된 컴포넌트 클래스를 사용하여 빠르고 일관된 UI 구성을 하고 있습니다.
- **하드코딩된 색상**: 일부 색상이 Tailwind config가 아닌 HTML 내에 하드코딩 되어 있습니다 (예: `bg-[#c8f097]`).
- **CDN 의존**: 빌드 과정 없이 CDN을 통해 라이브러리를 로드하고 있어 초기 로딩 속도나 오프라인 개발에 제약이 있을 수 있습니다.

### 1.3 문제점
1.  **규칙과의 불일치**: 프로젝트 규칙(`GEMINI.md`)에는 "bootstrap5 사용"이라고 명시되어 있으나, 실제 코드는 "Tailwind + DaisyUI"로 구현되어 있습니다. 이는 유지보수 시 혼란을 야기할 수 있습니다.
2.  **HTML 가독성 저하**: 유틸리티 클래스가 많아짐에 따라 HTML 코드가 복잡해지고, 비즈니스 로직(Alpine.js `x-data` 등)과 스타일 코드가 섞여 가독성이 떨어집니다.
3.  **중복 코드**: 비슷한 디자인의 버튼이나 카드가 여러 파일에 걸쳐 반복적으로 정의되어 있어 테마 변경 시 수정 범위가 넓어집니다.

---

## 2. 설계 개선 제안 (Better Design Direction)

프로젝트 규칙과 실제 코드의 괴리를 해소하고, `kiwi7` 프로젝트의 "정갈하고 아름다운 표현"이라는 목표를 달성하기 위해 아래 두 가지 방향 중 하나를 선택할 것을 제안합니다.

### [권장] 안 1: Tailwind CSS + DaisyUI 체제 확립 및 고도화

현재 이미 구축된 디자인 시스템(Tailwind+DaisyUI)이 현대적이고 개발 생산성이 높으므로, 이를 공식화하고 구조를 체계화하는 방향입니다.

**개선 방안:**
1.  **일관된 테마 적용**: 하드코딩된 색상(예: `#c8f097`)을 제거하고 DaisyUI의 Semantic Color(`primary`, `secondary`, `accent` 등)를 사용하여 다크모드/라이트모드 전환이 매끄럽게 되도록 합니다.
2.  **컴포넌트화**: 반복되는 UI 패턴(예: 주식 종목 카드, 계좌 리스트 아이템)을 Nunjucks의 `macro`나 별도의 HTML 템플릿 파일(`include`)로 분리하여 HTML의 복잡도를 낮춥니다.
3.  **Tailwind 설정 분리**: CDN 방식에서도 커스텀 설정을 사용할 수 있도록 `tailwind.config.js` 스크립트를 헤더에 체계적으로 관리합니다.
4.  **규칙 업데이트**: `GEMINI.md`의 규칙을 "bootstrap5"에서 "Tailwind CSS + DaisyUI"로 수정하여 혼란을 방지합니다.

### 안 2: Bootstrap 5로의 전면 회귀

프로젝트 초기 규칙인 "Bootstrap 5"를 엄격히 준수하기 위해 현재의 모든 Tailwind 코드를 걷어내고 Bootstrap으로 재작성하는 방향입니다.

**장점**:
- 기존 규칙 준수.
- 클래스명이 상대적으로 간결할 수 있음.

**단점**:
- **막대한 리팩토링 비용**: 현재 `main.html`, `nav.html` 등 주요 UI가 Tailwind 기반이므로 거의 모든 뷰 파일을 수정해야 합니다.
- **디자인 퀄리티 저하 위험**: DaisyUI가 제공하는 모던한 룩앤필을 Bootstrap 기본 테마로 다시 구현하려면 상당한 커스텀 CSS 작업이 필요합니다.

---

## 3. 결론 및 추천

**"[권장] 안 1: Tailwind CSS + DaisyUI 체제 확립"**을 추천합니다. 이미 코드가 Tailwind 기반으로 상당히 고도화되어 있으며, 이는 "빠르고 아름다운 UI 구현"이라는 목표에 더 부합합니다.

### 실행 로드맵
1.  **규칙 문서 수정**: `GEMINI.md`에 스타일 가이드를 Tailwind로 업데이트.
2.  **색상 상수화**: `nav.html` 등의 하드코딩된 색상을 Tailwind 테마 색상으로 대체.
3.  **헤더 정리**: `main.html` 등의 `<head>` 내 스타일 정의를 최소화하고 공통 설정(`config`)으로 이동.
