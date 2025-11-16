#전공 과목들에 대한 정보
Majorbasic = ["미분적분학","고급미분적분학","선형대수","미분방정식",
            "물리학및실험1","물리학및실험2","확률및랜덤변수","웹/파이썬프로그래밍",
            "객체지향프로그래밍및실습"]
Majorrequire = ["Adventure_Design","신호와시스템","물리전자",
                "논리회로","회로이론","전자회로1","기초회로실험",
                 "종합설계","졸업논문"]
Majorselete = ["디지털신호처리","마이크로프로세서","자료구조및알고리즘","머신러닝개론",
                "컴퓨터구조","컴퓨터네트워크","디지털통신","정보및부호이론","디지털회로설계및언어",
                "전자회로2","자동제어","전자기학2","반도체공학","반도체공정"]
Majorselete_experiment= ["전파통신실험","DSP실험","디지털집적회로모델링실험","전자회로실험","소프트웨어랩"]
Majorsadvance_circuit = ["VLSI_설계","임베디드시스템설계","반도체집적회로",
                        "로봇제어공학","Soc_설계"]
Majoradvance_signalsystem = ["이동통신","무선데이터통신","영상신호처리","실감미디어시스템"]
Majoradvance_semiconductor = ["광전자공학","디스플레이공학","고주파공학","안테나공학"]

related_keywords={}
related_keywords["반도체"]= ["반도체","소자","나노","광전자","디스플레이","MEMS","VLSI"]
related_keywords["회로"]= ["회로","임베디드","로봇","제어","시스템","SoC","마이크로프로세서"]
related_keywords["신호"]= ["신호","시스템","DSP","영상","미디어","머신러닝","통신","데이터","이동통신","무선","IoT"]
related_keywords["임베디드"]= ["임베디드","로봇","제어","시스템","SoC","마이크로프로세서","자동차","자율주행","드론","IoT"]


class Professor:
    def __init__(self, name, research, office_location):
        self.name = name
        self.research = research
        self.office_location = office_location


prof_list = [
    # 반도체 및 파동 연구그룹
    Professor("박욱", "Bio-MEMS, Multiscale fabrication, Anti-counterfeiting technology, PUFs, DNA storage, Encoded particle", "MultiplexON 403호"),
    Professor("백운식", "광신호처리, 홀로그래피, 생체공학", "416호"),
    Professor("예윤해", "광섬유 광학(광섬유 센서, 광통신용 부품), 간섭형 광섬유 센서, 신호처리 및 칩 설계 기술, 광섬유 가공 기술", "507호"),
    Professor("유재수", "나노반도체 및 광전소자 설계, 성장/제작, 패키징 및 측정기술", "503호"),
    Professor("이범선", "소형 및 배열안테나(광대역, 멀티밴드, MIMO, 위성 추진체 및 로켓 등), 메타물질, 무선전력전송", "611호"),
    Professor("이승현", "차세대 소자, 메모리 및 디스플레이", "518호"),
    Professor("김상혁", "전자파, 무선 전력 전송, Signal/Power Integrity, Microwave Imaging, mmWave Radar Technology", "408호"),
    Professor("김대원", "Energy Harvesting/Conversion/Storage System, Nano Bio-Electronic Device", "410호"),
    Professor("이응규", "에너지 & 포토닉스", "516호"),
    
    # 회로 및 시스템 연구그룹
    Professor("김동한", "Multi-agent Cooperation System, Human Robot Interaction (HRI)", "609호"),
    Professor("김진상", "영상 및 이동통신용 SoC, 회로 및 시스템설계, 나노공정을 이용한 우주국방용 VLSI 설계", "515호"),
    Professor("김창우", "MMIC 설계 및 제작, 이동/위성통신용 RF소자 및 회로설계 및 제작", "613호"),
    Professor("윤상웅", "High frequency integrated circuits, modules, and systems", "608호"),
    Professor("이종욱", "RFID 태그설계, 통신용 RF 회로설계, 밀리미터파 회로설계, 전력제어회로(PMIC) 설계", "617호"),
    Professor("장익준", "초저전력 VLSI 및 회로 설계, Nano 소자를 이용한 회로 설계, 차세대 메모리 연구", "519호"),
    Professor("정연모", "SoC Design, Embedded Systems, Digital Systems, Software Engineering", "405호"),
    Professor("홍상훈", "임베디드 메모리 설계, 저전력 인터페이스 회로 설계", "606호"),
    Professor("임영현", "저전력, 저잡음, 초소형 아날로그/RF 회로 설계 for 5G/6G통신, 사물인터넷", "608호"),
    Professor("최승규", "고성능/고에너지효율 시스템을 위한 소프트웨어-하드웨어 공동 설계, 인공지능 가속기 설계", "543-2호"),
    Professor("최우준", "스마트 센서 인터페이스 회로 설계, 바이오 메디컬 회로 및 시스템 설계, 초소형 컴퓨팅 플랫폼 설계", "우정원 7002호"),

    # 통신 및 신호처리 연구그룹
    Professor("김규헌", "디지털 멀티미디어 방송, 대화형 데이터 서비스 기술, 영항 및 동영상 처리", "501호"),
    Professor("김원하", "인간인지기반 멀티디디어 신호처리 및 부호화, 디지털방송응용기술", "517호"),
    Professor("김윤희", "무선/이동통신, 통신신호처리, 6G 물리계층 설계 및 지능화", "520호"),
    Professor("김정근", "무선네트워크", "525호"),
    Professor("서덕영", "Networked Media, Mobile Multimedia, MPEG/3GPP Standardization", "401호"),
    Professor("손원", "디지털방송, 위성통신, 신호처리", "521호"),
    Professor("송주빈", "무선통신 및 네트워킹, 최적자원할당기술, Cognitive Radio Networking, Cyber Physical Systems, Internet of Things, Smart Grid", "615호"),
    Professor("신현동", "무선통신, 양자정보 및 컴퓨팅", "513호"),
    Professor("이계산", "차세대 이동통신, OFDM, MC-CDMA, MC-DS/CDMA, Visible Light Communication, LED 통신", "505호"),
    Professor("정해준", "무선통신, 신호처리, 지능형 네트워크, 무선전력 전송", "514호"),
    Professor("최민석", "Wireless Distributed System (Wireless Caching, Edge Computing, Distributed Learning), Federated Learning, Reinforcement Learning, Network Optimization, Content Delivery and Video Streaming", "510호"),
    Professor("홍인기", "이동통신시스템 물리채널, 스펙트럼 엔지니어링, Cross-layer Engineering", "523호"),
    Professor("고한얼", "5G/6G 모바일 코어 네트워크, 네트워크 자동화, 모바일 엣지 컴퓨팅, SDN, IoT", "416호"),
    Professor("최기호", "Video/Image/Multimedia Coding and Processing, Deep Learning based Multimedia Coding and Processing, Multimedia Standardization", "410호")
]
INTEREST_COURSE_MAP = {
    "회로": ["회로이론", "전자회로1", "전자회로2", "디지털회로설계및언어", "기초회로실험", "회로이론2", "VLSI_설계", "임베디드시스템설계", "반도체집적회로", "로봇제어공학", "Soc_설계"],
    "반도체": ["물리전자", "반도체공학", "반도체공정", "VLSI_설계", "반도체집적회로", "광전자공학", "디스플레이공학"],
    "신호": ["신호와시스템", "디지털신호처리", "DSP실험", "영상신호처리", "실감미디어시스템", "머신러닝개론"],
    "통신": ["확률및랜덤변수", "디지털통신", "정보및부호이론", "전파통신실험", "이동통신", "무선데이터통신", "안테나공학", "고주파공학"],
    "컴퓨터": ["웹/파이썬프로그래밍", "객체지향프로그래밍및실습", "자료구조및알고리즘", "컴퓨터구조", "컴퓨터네트워크", "소프트웨어랩", "머신러닝개론"],
    "AI": ["머신러닝개론", "자료구조및알고리즘", "디지털신호처리", "영상신호처리"],
    "로봇": ["로봇제어공학", "자동제어", "마이크로프로세서"]

}
