#!/usr/bin/env python3
"""
API Definition Files Formatter

KIS/LS 증권 API 정의 파일들을 일관된 JSON 스타일로 포맷팅하는 도구
requests, responses 폴더 모두 지원

사용법:
    # 모든 definition 폴더 포맷팅
    python3 tools/definition_format.py --all

    # 특정 폴더 포맷팅
    python3 tools/definition_format.py backend/domains/kis/models/requests

    # 단일 파일 포맷팅
    python3 tools/definition_format.py backend/domains/kis/models/requests/market_etf.py
"""

import os
import sys
import argparse
import re
from typing import Dict, Any, List, Tuple


class DefinitionFormatter:
    """API Definition 파일 포맷터"""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.files_processed = 0
        self.files_skipped = 0
        self.errors = []

    def format_file(self, filepath: str) -> Tuple[bool, str]:
        """단일 파일 포맷팅"""
        if not filepath.endswith('.py'):
            return False, "Python 파일이 아님"

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # 변수명과 딕셔너리 추출
            match = re.search(r'(\w+_REQUESTS|\w+_RESPONSES|\w+_DEFINITIONS|\w+_ETF|\w+_ELW)\s*=\s*(\{.*\})', content, re.DOTALL)
            if not match:
                return False, "정의 변수를 찾을 수 없음"

            var_name = match.group(1)
            dict_str = match.group(2)

            # 딕셔너리 파싱 - null을 None으로 변환
            try:
                # null -> None 변환 (JSON style to Python)
                dict_str_fixed = dict_str.replace(': null', ': None')
                data = eval(dict_str_fixed)
            except Exception as e:
                return False, f"파싱 실패: {str(e)[:50]}"

            # 파일 유형 감지
            file_type = self._detect_file_type(data)

            # 포맷팅
            formatted_content = self._format_content(var_name, data, file_type)

            # 파일 쓰기
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(formatted_content)

            self.files_processed += 1
            return True, f"완료 ({file_type})"

        except Exception as e:
            self.errors.append((filepath, str(e)))
            return False, f"오류: {str(e)[:30]}"

    def _detect_file_type(self, data: Dict) -> str:
        """파일 유형 감지"""
        if not data:
            return "UNKNOWN"

        first_value = next(iter(data.values()))

        if isinstance(first_value, dict):
            if 'tr_cd' in first_value:
                return "LS"
            elif 'tr_id' in first_value:
                return "KIS"
            elif 'blocks' in first_value:
                return "LS"
            elif 'query' in first_value or 'path' in first_value:
                return "KIS"

        return "UNKNOWN"

    def _format_content(self, var_name: str, data: Dict[str, Any], file_type: str) -> str:
        """데이터를 포맷팅된 Python 코드로 변환"""
        lines = [
            '# Auto-generated',
            'from typing import Any, Dict, List',
            '',
            f'{var_name} = {{',
        ]

        for key in sorted(data.keys()):
            value = data[key]
            lines.extend(self._format_entry(key, value, file_type))
            lines.append("    },")

        # 마지막 쉼표 제거
        if lines[-1].endswith(','):
            lines[-1] = lines[-1].rstrip(',')

        lines.append("}")
        lines.append("")

        return "\n".join(lines)

    def _format_entry(self, key: str, value: Dict[str, Any], file_type: str) -> List[str]:
        """항목 포맷팅"""
        lines = [f"    '{key}': {{"]

        # 필드 순서 정의
        if file_type == "KIS":
            field_order = ['method', 'title', 'tr_id', 'url', 'path', 'query']
        else:
            field_order = ['tr_cd', 'title', 'blocks', 'fields']

        # 순서대로 출력
        for field in field_order:
            if field in value:
                lines.append(self._format_field(field, value[field], indent=2))

        # 나머지 필드
        for field in sorted(value.keys()):
            if field not in field_order:
                lines.append(self._format_field(field, value[field], indent=2))

        # 마지막 쉼표 제거
        if lines[-1].endswith(','):
            lines[-1] = lines[-1].rstrip(',')

        return lines

    def _format_field(self, name: str, value: Any, indent: int = 1) -> str:
        """필드 포맷팅"""
        indent_str = " " * (indent * 4)
        next_indent_str = " " * ((indent + 1) * 4)

        if isinstance(value, str):
            safe_value = value.replace("'", "\\'")
            return f"{indent_str}'{name}': '{safe_value}',"

        elif isinstance(value, bool):
            return f"{indent_str}'{name}': {value},"

        elif isinstance(value, (int, float)):
            return f"{indent_str}'{name}': {value},"

        elif isinstance(value, list):
            if not value:
                return f"{indent_str}'{name}': [],"

            lines = [f"{indent_str}'{name}': ["]

            for i, item in enumerate(value):
                if isinstance(item, dict):
                    lines.append(f"{next_indent_str}{{")
                    for k in sorted(item.keys()):
                        v = item[k]
                        if isinstance(v, str):
                            safe_v = v.replace("'", "\\'")
                            lines.append(f"{next_indent_str}    '{k}': '{safe_v}',")
                        else:
                            lines.append(f"{next_indent_str}    '{k}': {v},")

                    if lines[-1].endswith(','):
                        lines[-1] = lines[-1].rstrip(',')

                    lines.append(f"{next_indent_str}}}{',' if i < len(value) - 1 else ''}")
                else:
                    lines.append(f"{next_indent_str}{repr(item)}{',' if i < len(value) - 1 else ''}")

            lines.append(f"{indent_str}],")
            return "\n".join(lines)

        elif isinstance(value, dict):
            if not value:
                return f"{indent_str}'{name}': {{}},"

            lines = [f"{indent_str}'{name}': {{"]

            for k in sorted(value.keys()):
                v = value[k]
                if isinstance(v, str):
                    safe_v = v.replace("'", "\\'")
                    lines.append(f"{next_indent_str}'{k}': '{safe_v}',")
                elif isinstance(v, dict):
                    lines.append(f"{next_indent_str}'{k}': {{")
                    for kk in sorted(v.keys()):
                        vv = v[kk]
                        if isinstance(vv, str):
                            safe_vv = vv.replace("'", "\\'")
                            lines.append(f"{next_indent_str}    '{kk}': '{safe_vv}',")
                        else:
                            lines.append(f"{next_indent_str}    '{kk}': {vv},")
                    if lines[-1].endswith(','):
                        lines[-1] = lines[-1].rstrip(',')
                    lines.append(f"{next_indent_str}}},")
                elif isinstance(v, list):
                    lines.append(f"{next_indent_str}'{k}': {repr(v)},")
                else:
                    lines.append(f"{next_indent_str}'{k}': {v},")

            if lines[-1].endswith(','):
                lines[-1] = lines[-1].rstrip(',')

            lines.append(f"{indent_str}}},")
            return "\n".join(lines)

        else:
            return f"{indent_str}'{name}': {repr(value)},"

    def format_directory(self, dirpath: str) -> None:
        """디렉토리의 모든 Python 파일 포맷팅"""
        if not os.path.isdir(dirpath):
            print(f"❌ 디렉토리를 찾을 수 없습니다: {dirpath}")
            return

        py_files = sorted([f for f in os.listdir(dirpath) if f.endswith('.py')])

        if not py_files:
            print(f"⚠️  Python 파일이 없습니다: {dirpath}")
            return

        print(f"\n📂 {dirpath}")
        print("=" * 80)

        for filename in py_files:
            filepath = os.path.join(dirpath, filename)
            success, message = self.format_file(filepath)

            if success:
                print(f"✅ {filename:45s} {message}")
            else:
                print(f"⏭️  {filename:45s} {message}")
                self.files_skipped += 1

    def format_all_definitions(self, base_dir: str = "backend/domains") -> None:
        """모든 definition 폴더 포맷팅"""
        dirs_to_format = [
            f"{base_dir}/kis/models/requests",
            f"{base_dir}/kis/models/responses",
            f"{base_dir}/ls/models/requests",
            f"{base_dir}/ls/models/responses",
        ]

        for dirpath in dirs_to_format:
            if os.path.isdir(dirpath):
                self.format_directory(dirpath)

    def print_summary(self) -> None:
        """작업 요약 출력"""
        print("\n" + "=" * 80)
        print("📊 작업 요약")
        print("=" * 80)
        print(f"✅ 포맷팅 완료: {self.files_processed} 파일")
        print(f"⏭️  건너뜀: {self.files_skipped} 파일")

        if self.errors:
            print(f"\n❌ 오류 발생: {len(self.errors)} 파일")
            for filepath, error in self.errors[:5]:
                print(f"   - {os.path.basename(filepath)}: {error[:40]}")
            if len(self.errors) > 5:
                print(f"   ... 외 {len(self.errors) - 5}개 파일")
        else:
            print(f"\n✨ 모든 파일이 성공적으로 처리되었습니다!")


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(
        description="API Definition 파일 포맷터 - KIS/LS requests/responses 폴더 지원",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  python3 tools/definition_format.py --all                          # 모든 폴더 포맷팅
  python3 tools/definition_format.py backend/domains/kis/models/requests
  python3 tools/definition_format.py backend/domains/kis/models/requests/market_etf.py
        """
    )

    parser.add_argument('path', nargs='?', help='포맷팅할 파일 또는 디렉토리 경로')
    parser.add_argument('--all', action='store_true', help='모든 definition 폴더 포맷팅')
    parser.add_argument('-v', '--verbose', action='store_true', help='자세한 정보 출력')

    args = parser.parse_args()

    # 프로젝트 루트로 이동
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    os.chdir(project_root)

    formatter = DefinitionFormatter(verbose=args.verbose)

    if args.all:
        formatter.format_all_definitions()
    elif args.path:
        if os.path.isfile(args.path):
            print(f"\n📄 파일 포맷팅: {args.path}")
            success, message = formatter.format_file(args.path)
            print(f"{'✅' if success else '❌'} {message}")
        elif os.path.isdir(args.path):
            formatter.format_directory(args.path)
        else:
            print(f"❌ 경로를 찾을 수 없습니다: {args.path}")
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(0)

    formatter.print_summary()


if __name__ == '__main__':
    main()
