"""Auto-generated definition file"""

from typing import Any, Dict

from .responses.kis_resp_1 import KIS_RESPONSE_DEF_1
from .responses.kis_resp_2 import KIS_RESPONSE_DEF_2
from .responses.kis_resp_3 import KIS_RESPONSE_DEF_3
from .responses.kis_resp_4 import KIS_RESPONSE_DEF_4
from .responses.kis_resp_5 import KIS_RESPONSE_DEF_5
from .responses.kis_resp_6 import KIS_RESPONSE_DEF_6
from .responses.kis_resp_7 import KIS_RESPONSE_DEF_7

KIS_RESPONSE_DEF = {}
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_1)
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_2)
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_3)
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_4)
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_5)
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_6)
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_7)


def get_response_definition(api_id: str) -> Dict[str, Any]:
  return KIS_RESPONSE_DEF.get(api_id)


def get_response_fields(api_id: str) -> list:
  """API의 모든 output 필드를 통합하여 반환"""
  resp = get_response_definition(api_id)
  if not resp:
    return []

  fields = []
  # response_def의 각 키를 순회하며 fields 수집
  for key, value in resp.items():
    if isinstance(value, dict) and 'fields' in value and isinstance(value['fields'], list):
      fields.extend(value['fields'])

  return fields


def get_field_name(api_id: str, key: str) -> str:
  """필드 키에 해당하는 한글 이름을 반환"""
  resp = get_response_definition(api_id)
  if not resp:
    return key

  # 모든 output의 fields를 순회하며 key 찾기
  for output_key, output_value in resp.items():
    if isinstance(output_value, dict):
      # 일반 필드 (rt_cd, msg_cd, msg1 등)
      if output_key == key and 'name' in output_value:
        return output_value['name']
      # output, output1, output2 등의 fields
      if 'fields' in output_value and isinstance(output_value['fields'], list):
        for field in output_value['fields']:
          if field.get('key') == key:
            return field.get('name', key)

  return key
