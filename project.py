# 전자공학과 학생들을 위한 수강 가이드라인 제공 챗봇 알고리즘 프로젝트
#엔지니어스웨이



class GetClass():
    def __init__(self):
        self.Majorbasic_attended = []
        self.Majorrequire_attended = []
        self.Majorselete_attended = []
        #전공 과목들 중 수강완료한 과목들을 저장할 리스트들


        self.Majorbasic = ["미분적분학","고급미분적분학","선형대수","미분방정식",
                      "물리학및실험1","물리학및실험2","확률및랜덤변수","웹/파이썬프로그래밍",
                      "객체지향프로그래밍및실습"]
        self.Majorrequire = ["Adventure_Design","신호와시스템","물리전자",
                             "논리회로","회로이론","전자회로1","기초회로실험",
                             "종합설계","졸업논문"]
        self.Majorselete = ["디지털신호처리","마이크로프로세서","자료구조및알고리즘","머신러닝개론",
                            "컴퓨터구조","컴퓨터네트워크","디지털통신","정보및부호이론","디지털회로설계및언어",
                            "전자회로2","자동제어","전자기학2","반도체공학","반도체공정","회로이론2"]
        self.Majorselete_others = ["전파통신실험","DSP실험","디지털집적회로모델링실험","전자회로실험","소프트웨어랩"]
        self.Majorsadvance_circuit = ["VLSI_설계","임베디드시스템설계","반도체집적회로",
                                    "로봇제어공학","Soc_설계"]
        self.Majoradvance_signalsystem = ["이동통신","무선데이터통신","영상신호처리","실감미디어시스템"]
        self.Majoradvance_semiconductor = ["광전자공학","디스플레이공학","고주파공학","안테나공학"]

        self.must_attend_Majorrequire = []
        self.must_attend_Majorselete = []
        self.must_attend_Majorselete_others = []
        self.must_attend_Majorsadvance_circuit = []
        self.must_attend_Majoradvance_signalsystem = []
        self.must_attend_Majoradvance_semiconductor = []

    def save_Major(self,major):
        self.major = major
        return(f"사용자님의 전공은 {major}입니다.")
    
    def save_attended_Majorbasic_classes(self,classes): #전공 기초 과목들 중 수강완료한 과목들을 입력받고, self.majorbasic_attended에 저장함
        print('전공기초 과목들은 ["미분적분학","고급미분적분학","선형대수","미분방정식","물리학및실험1","물리학및실험2","확률및랜덤변수","웹/파이썬프로그래밍","객체지향프로그래밍및실습"]입니다.')
        if classes in self.Majorbasic:
            if classes not in self.Majorbasic_attended: #전공 기초 과목들에 있으며, 이미 수강하지도 않은 과목
                self.Majorbasic_attended.append(classes)
            else: #전공 기초 과목에 있지만, 이미 수강 완료된 과목
                return("이미 수강 완료된 수업입니다.")
        else:#전공 기초 과목에 없는 과목
            print("전공기초 목록에 있는 과목들이 아닙니다.")

    def must_attend_Majorbasic_classes(self):
        for i in self.Majorbasic:
            if i not in self.Majorbasic_attended:
                self.must_attend_Majorrequire.append(i)
        print("전공기초 과목들 중 수강해야하는 과목들은 다음과 같습니다.")
        return self.must_attend_Majorrequire
    
    def save_attended_Majorrequire_classes(self,classes): #전공 필수 과목들 중 수강완료한 과목들을 입력받고, self.majorrequire_attended에 저장함
        print('전공필수 과목들은 ["Adventure_Design","신호와시스템","물리전자","논리회로"]입니다.')
        if classes in self.Majorrequire:
            if classes not in self.Majorrequire_attended: #전공 필수 과목들에 있으며, 이미 수강하지도 않은 과목
                self.Majorrequire_attended.append(classes)
            else: #전공 필수 과목에 있지만, 이미 수강 완료된 과목
                return("이미 수강 완료된 수업입니다.")
        else:#전공 필수 과목에 없는 과목
            print("전공필수 목록에 있는 과목들이 아닙니다.")

    def must_attend_Majorrequire_classes(self):
        for i in self.Majorrequire:
            if i not in self.Majorrequire_attended:
                self.must_attend_Majorrequire.append(i)
        print("전공필수 과목들 중 수강해야하는 과목들은 다음과 같습니다.")
        return self.must_attend_Majorrequire
    
    def save_attended_Majorselete_classes(self,classes): #전공 선택 과목들 중 수강완료한 과목들을 입력받고, self.majorselete_attended에 저장함
        print('전공선택 과목들은 ["디지털신호처리","마이크로프로세서","자료구조및알고리즘","머신러닝개론","컴퓨터구조","컴퓨터네트워크","디지털통신","정보및부호이론","디지털회로설계및언어","전자회로2","자동제어","전자기학2","반도체공학","반도체공정","회로이론2"]입니다.')
        if classes in self.Majorselete :
            if classes not in self.Majorselete_attended: #전공 선택 과목들에 있으며, 이미 수강하지도 않은 과목
                self.Majorselete_attended.append(classes)
            else: #전공 선택 과목에 있지만, 이미 수강 완료된 과목
                return("이미 수강 완료된 수업입니다.")
        else:#전공 선택 과목에 없는 과목
            print("전공선택 목록에 있는 과목들이 아닙니다.")
    
    def save_attended_Majorselete_others_classes(self,classes): #전공 선택 과목들 중 수강완료한 과목들을 입력받고, self.majorselete_attended에 저장함
        print('전공선택 기타 과목들은 ["전파통신실험","DSP실험","디지털집적회로모델링실험","전자회로실험","소프트웨어랩"]입니다.')
        if classes in self.Majorselete_others :
            if classes not in self.Majorselete_attended: #전공 선택 과목들에 있으며, 이미 수강하지도 않은 과목
                self.Majorselete_attended.append(classes)
            else: #전공 선택 과목에 있지만, 이미 수강 완료된 과목
                return("이미 수강 완료된 수업입니다.")
        else:#전공 선택 과목에 없는 과목
            print("전공선택 기타 목록에 있는 과목들이 아닙니다.")
    
    def save_attended_Majorsadvance_circuit_classes(self,classes): #전공 심화 과목들 중 수강완료한 과목들을 입력받고, self.majorsadvance_circuit_attended에 저장함
        print('전공심화(회로) 과목들은 ["VLSI_설계","임베디드시스템설계","반도체집적회로","로봇제어공학","Soc_설계"]입니다.')
        if classes in self.Majorsadvance_circuit :
            if classes not in self.Majorselete_attended: #전공 심화 과목들에 있으며, 이미 수강하지도 않은 과목
                self.Majorselete_attended.append(classes)
            else: #전공 심화 과목에 있지만, 이미 수강 완료된 과목
                return("이미 수강 완료된 수업입니다.")
        else:#전공 심화 과목에 없는 과목
            print("전공심화(회로) 목록에 있는 과목들이 아닙니다.")
    

    def save_attended_Majoradvance_signalsystem_classes(self,classes): #전공 심화 과목들 중 수강완료한 과목들을 입력받고, self.majoradvance_signalsystem_attended에 저장함
        print('전공심화(신호처리) 과목들은 ["이동통신","무선데이터통신","영상신호처리","실감미디어시스템"]입니다.')
        if classes in self.Majoradvance_signalsystem :
            if classes not in self.Majorselete_attended: #전공 심화 과목들에 있으며, 이미 수강하지도 않은 과목
                self.Majorselete_attended.append(classes)
            else: #전공 심화 과목에 있지만, 이미 수강 완료된 과목
                return("이미 수강 완료된 수업입니다.")
        else:#전공 심화 과목에 없는 과목
            print("전공심화(신호처리) 목록에 있는 과목들이 아닙니다.")
    
    def save_attended_Majoradvance_semiconductor_classes(self,classes): #전공 심화 과목들 중 수강완료한 과목들을 입력받고, self.majoradvance_semiconductor_attended에 저장함    
        print('전공심화(반도체) 과목들은 ["광전자공학","디스플레이공학","고주파공학","안테나공학"]입니다.')
        if classes in self.Majoradvance_semiconductor :
            if classes not in self.Majorselete_attended: #전공 심화 과목들에 있으며, 이미 수강하지도 않은 과목
                self.Majorselete_attended.append(classes)
            else: #전공 심화 과목에 있지만, 이미 수강 완료된 과목
                return("이미 수강 완료된 수업입니다.")
        else:#전공 심화 과목에 없는 과목
            print("전공심화(반도체) 목록에 있는 과목들이 아닙니다.")
            
                
