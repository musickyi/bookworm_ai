import json
from openai import OpenAI
client = OpenAI()

json_data = [
  {
    "comments": "송중기 시대극은 믿고본다. 첫회 신선하고 좋았다.",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "지현우 나쁜놈",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "알바쓰고많이만들면되지 돈욕심없으면골목식당왜나온겨 기댕기게나하고 산에가서팔어라",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "hate"
  },
  {
    "comments": "설마 ㅈ 현정 작가 아니지??",
    "contain_gender_bias": "True",
    "bias": "gender",
    "hate": "hate"
  },
  {
    "comments": "이미자씨 송혜교씨 돈이 그리 많으면 탈세말고 그돈으로 평소에 불우이웃에게 기부도 좀 하고사시죠.",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "일베충들 ㅂㄷ거리는것봐라 ㅉㅉ",
    "contain_gender_bias": "False",
    "bias": "others",
    "hate": "hate"
  },
  {
    "comments": "아이즈원 힘내세요...일본 진출도 했으니 일본서 좋은 모습 보여줘도 팬들은 응원 합니다.",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "강부자 선생님 전미선 비보에 오열을 하셨다니 눈물이 나네요 힘내세요",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "알았어 그만",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "이영자씨는 진정성 있는거라면 녹화불참으로 끝내지말고 자진하차해라 시청자는 고려도 안하고 일방적 불참은 아닌듯 엠비씨도 시청율 좋아서 고민하는거 같은데 결방할게 아니고 폐지해라",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "이경규가 이런거보면 세련되긴함 저 나이에 차은우 누가 알꼬 아무리 잘생겼다해도. 배워야할점 많으신분",
    "contain_gender_bias": "False",
    "bias": "others",
    "hate": "none"
  },
  {
    "comments": "아c발 어쩌라고 뭔기사가계속나오냐",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "hate"
  },
  {
    "comments": "진짜 멋지네요~",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "명수 응근슬쩍 뒷치기각잡네",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "철구한테 별풍쏜놈 수준도 똑같지 뭐 ㅋㅋ",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "둘이 화장실가서 싸우길",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "송이매니저 거지냐 치과치료비용까지 남한테 타서 하게. 솔직히 치아관리를 얼마나 안했으면 앞니가 시커멓게 될따까지 냅두냐 치과공포증은 핑계지 볼때마다 얼마나 거슬리는데 쟤네 부모님은 뭐하나 앞니하나 치료도 못해주고?",
    "contain_gender_bias": "False",
    "bias": "others",
    "hate": "hate"
  },
  {
    "comments": "언제까지 반일 감정에 불탈래 막상 역사도 그렇게 모르는 개돼지들이 꼭 흥분하더라",
    "contain_gender_bias": "False",
    "bias": "others",
    "hate": "hate"
  },
  {
    "comments": "기자왜이래? 이건 아니야 니 일기장에 써라 제목부터 오바야",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "hate"
  },
  {
    "comments": "이거 아직도 하?",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "조우종이가 장성규보단 낫지~장성규 얼마못간다",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "주말드라마에 장사하는엄마가 폐암걸리는 드라마를볼줄이야...",
    "contain_gender_bias": "False",
    "bias": "others",
    "hate": "none"
  },
  {
    "comments": "난 남자쪽에서 여자를 버렸다는줄 알았는데 자세히 보니까 여자쪽 집에서 남자를 버린것 같은데... 버려놓고 이제와서?;;;",
    "contain_gender_bias": "True",
    "bias": "gender",
    "hate": "offensive"
  },
  {
    "comments": "언플 오지네 진짜 ! 언플하기전에 연기력과겸손함부터 쳐배워라 !",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "hate"
  },
  {
    "comments": "한화이글스 해산하자!!! 丕빱♡",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "hate"
  },
  {
    "comments": "유이 자연스러워진 연기",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "알겠으니까 이제는 좀 조용히좀 살아 진짜 관종이네ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "죽창 운운하면서 반일선동하는 뒤로 자기들은 일제 쓸거 다 쓰는 한국 정치인들이나, 간악한 쪽XX 운운 하면서 즈그들은 렉서스 끌고 일제 전자기기 쓰는 북한놈들이나 ㅋㅋㅋㅋ 순진하게 부화뇌동하는 국민들만 바보되는거지 ㅋㅋㅋㅋ",
    "contain_gender_bias": "False",
    "bias": "others",
    "hate": "hate"
  },
  {
    "comments": "서현진 이민기 둘다 연기가 식상함",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "임신했나보네 몸안좋아서 임신안되는줄 알았는데 우울하다 왜 딴따라들은 임신잘되고 나만안되는데",
    "contain_gender_bias": "False",
    "bias": "others",
    "hate": "hate"
  },
  {
    "comments": "왜 유재석에게는 얼굴에 케익폭탄인가 그 벌칙 안하는거지?",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "유승준은 천재적인 재능이라도 있지 이넘은 뭐없잖어 대중들이 왜 봐줘야해",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "hate"
  },
  {
    "comments": "왜 현우한테 ㅠㅜ",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "ㅋ 여기 댓글은 tv조선 직원들이 동원됐나여?",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "그래도 17 18 19회분은 보여주는게",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "누가 그랬다. 한국 사람들에게 마음의 문을 열고 진심을 다해 대하면 그 한국 사람은 사기칠 생각부터 한다고...",
    "contain_gender_bias": "False",
    "bias": "others",
    "hate": "offensive"
  },
  {
    "comments": "남자는 애걸복걸한 여자를 좋아하지않는데 박나래도 알텐데 그냥 쇼맨쉽인가",
    "contain_gender_bias": "True",
    "bias": "gender",
    "hate": "offensive"
  },
  {
    "comments": "이승기 예능 이끌 능력도없는데 팬을위한프론가보네",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "캡쳐할 인간들 수두룩이네ㅋㅋ",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "둘다 비교하면서 들어봤는데 곡의 장르 분위기만 비슷하다고 느낄수있는데 표절은 아니다...그냥 가수 목소리만 비슷하네 창법이 비슷해서 혼돈 할수도 있을듯...",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "지인들끼리 밥내기 골프정도는 안하나? 기레기 어떻게든 엮으려고 하네...",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "hate"
  },
  {
    "comments": "꺼져주세요.. ㅈㄴ보기싫네",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "hate"
  },
  {
    "comments": "문재앙놈 땜에 애꿎은 젊은이들만 희생을 당하네~~~",
    "contain_gender_bias": "False",
    "bias": "others",
    "hate": "hate"
  },
  {
    "comments": "스포츠예능에 약쟁이라니?",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "간이 덜컥 빠지는 소리. 컥 세종아 너만은 아니길.",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "듣보잡 이지만 축하",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "하여간 죳티즌들 지들만 양반인척 역겹ㅋㅋㅋㅋ",
    "contain_gender_bias": "False",
    "bias": "others",
    "hate": "hate"
  },
  {
    "comments": "여자 두명이면 서로 까고 세명이면 둘이 하나깜",
    "contain_gender_bias": "True",
    "bias": "gender",
    "hate": "hate"
  },
  {
    "comments": "손예진이랑 소지섭이랑 곧 결혼한다 이글은 곧 성지글이 된다.",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "한혜진 진짜 성격은 모르겠고 방송이미지는 여자들이 좋아할 성격임 남자들이 볼땐 그냥 친구란 생각밖에 안들고 물론 좋은 성격인거 같긴함 방송 이미지대로라면",
    "contain_gender_bias": "True",
    "bias": "gender",
    "hate": "none"
  },
  {
    "comments": "꼰대베플만있나하고 연령대봤더니 3-40대들이 대부분..",
    "contain_gender_bias": "False",
    "bias": "others",
    "hate": "offensive"
  },
  {
    "comments": "효녀라 좋았는데...혜나 미워하는 인간들은 뭐지!!",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "머리가 삼발이라 짜잖아서 보기싫다",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "일반인은 귀찮아서 비추도 안 찍는다. 견제 질투빠 수작질에 질린다",
    "contain_gender_bias": "False",
    "bias": "others",
    "hate": "offensive"
  },
  {
    "comments": "디패 추가공식입장내길바란다 저렇게 무성의하게 조작됐고 아는바없다만 올리지말고..내부든 외부든 누가조작했는지 밝혀내겠다 혼선드려 죄송하다 두사람에게 사과한다 등 내야하는거 아닌가",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "아니라자나!!! 아 놔 진짜 난 팬도 아닌데다 짜증나네 이것 말고 웟대가리들이나 파라고!!!",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "조금 헷갈리긴 하지만 자세히 들어보면 다 맞출 수 있던데..ㅎㅎ",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "미친 이게 왜 문통 잘못이냐 덮긴 뭘덮어",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "언니 토닥토닥.....응원해욧~!!",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "고현정 연기 미모 카리스마 소름 !!! 드라마 잘 안보는데 오늘 첨 봤지만 시간가는줄 모르고 몰입했네요",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "정해인도 닮은듯?",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "여기 고소할 악풀러들 많네~~~",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "김태리 정말 연기잘해 진짜",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "현지 반응 별로던데 노래도 이상하고 춤도 난해하다고.. 국내에서도 지코한테 1위 다 뺏긴거보면 국내반응도 별로인듯..",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "임현주한테 열폭부리는 것들 많넼ㅋㅋ 하긴 지들은 임현주가 가진 매력의 반의반도없으니 남자못꼬시지",
    "contain_gender_bias": "True",
    "bias": "gender",
    "hate": "hate"
  },
  {
    "comments": "삼가 고인의 명복을 빕니다.",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "오 여판사네",
    "contain_gender_bias": "True",
    "bias": "gender",
    "hate": "offensive"
  },
  {
    "comments": "요즘은 용기있는 남자가 없는 듯.. 이러다 손예진 연애도 못하겠네^^;;",
    "contain_gender_bias": "True",
    "bias": "gender",
    "hate": "offensive"
  },
  {
    "comments": "힘내셔요~남들이 뭐라하든 열심히 살면 됩니다앞으로 좋은일만 가득하세요",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "그냥 김치석 따로 만들어라. 지적 장애인 대우 해주께 ㅋㅋㅋㅋ",
    "contain_gender_bias": "True",
    "bias": "gender",
    "hate": "hate"
  },
  {
    "comments": "짠돌이보단 낫다",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "짠내투어 멤버로 랩퍼 도끼를 추천합니다. 근검절약의 아이콘 이시더라고요",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
  {
    "comments": "너무 예쁘다 행복하세요♡♡♡",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "none"
  },
  {
    "comments": "ㅈㄹ 하고 자빠졋네..판빙빙 얼굴바 뭐 하냐...탈세 자랑스러운 일이냐?",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "hate"
  },
  {
    "comments": "본판이 예쁘시니 뭐ㅜ",
    "contain_gender_bias": "False",
    "bias": "none",
    "hate": "offensive"
  },
]

def convert_to_openai_chat_format(data):
    if data["contain_gender_bias"] == "False" and data["bias"] == "none" and data["hate"] == "none":
        content = "유해하지 않는 문장입니다."
    else:
        content = "유해한 문장입니다."
    return {"role": "user", "content": f"{data['comments']} {content}"}

openai_chat_format_data = [convert_to_openai_chat_format(data) for data in json_data]

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages = openai_chat_format_data
)