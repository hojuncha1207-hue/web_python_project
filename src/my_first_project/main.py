from data import (
    Majorbasic, Majorrequire, Majorselete, Majorselete_experiment, 
    Majorsadvance_circuit, Majoradvance_signalsystem, Majoradvance_semiconductor,
    Professor, prof_list,related_keywords,INTEREST_COURSE_MAP)
from typing import List, Dict, Optional, Set

class EEStudent_Info:
    def __init__(self, all_professors: List[Professor]):
        self.course_basic = set(Majorbasic)
        self.course_required = set(Majorrequire)
        self.course_select = set(Majorselete)
        self.course_select_experiment = set(Majorselete_experiment)
        self.course_advanced_circuit = set(Majorsadvance_circuit)
        self.course_advanced_signalsystem = set(Majoradvance_signalsystem)
        self.course_advanced_semiconductor = set(Majoradvance_semiconductor)
        
        self.all_professors = all_professors
        
        self.school_year: Optional[int]
        self.interested: Optional[str] 
        self.attended_classes: Set[str] = set()

    def get_student_interest(self, school_year: int, interested: str):
        self.school_year = school_year
        self.interested = interested

    def set_attended_classes(self, attended_list: List[str]):
        self.attended_classes = {subject.strip() for subject in attended_list}

    def recommend_remaining_by_category(self, category_name: str) -> List[str]:
        category_map = {
            "전공기초": self.course_basic,
            "전공필수": self.course_required,
            "전공선택": self.course_select,
            "전공선택_실험": self.course_select_experiment,
            "회로심화": self.course_advanced_circuit,
            "신호시스템심화": self.course_advanced_signalsystem,
            "반도체심화": self.course_advanced_semiconductor
        }
        
        if category_name not in category_map:
            return [f"'{category_name}'라는 카테고리가 없습니다."]
            
        all_courses_in_category = category_map[category_name]
        
        remaining = all_courses_in_category - self.attended_classes
        
        return sorted(list(remaining))

    def recommend_professors_by_interest(self) -> List[Professor]:
        if not self.interested:
            return []
            
        smart_keywords = self._get_keywords_from_interest()
        
        if not smart_keywords:
            return []
            
        matched_professors = []
        added_prof_names = set() 
        
        for professor in self.all_professors:
            for keyword in smart_keywords:
                if keyword.lower() in professor.research.lower():
                    if professor.name not in added_prof_names:
                        matched_professors.append(professor)
                        added_prof_names.add(professor.name)
                    break 
                        
        return matched_professors

    def recommend_classes_by_interest(self) -> (Set[str], Set[str]):
        if not self.interested:
            return set(), set()

        smart_keywords = self._get_keywords_from_interest() 
        recommended_courses = set()

        for interest_key, courses in INTEREST_COURSE_MAP.items():
            for keyword in smart_keywords:
                if keyword.lower() in interest_key.lower():
                    recommended_courses.update(courses)
                    break 

        attended_recommendations = recommended_courses.intersection(self.attended_classes)
        
        return recommended_courses, attended_recommendations
    
    def _get_keywords_from_interest(self) -> Set[str]:
        if not self.interested:
            return set()

        keyword_to_find = self.interested.lower()
        keyword_set = related_keywords.get(self.interested)
        if keyword_set:
            return set(keyword_set) 
        for key, values in related_keywords.items():
            if keyword_to_find in [interest.lower() for interest in values]:
                return set(related_keywords[key]) 
        return {keyword_to_find}
        
    def analyze_interest_match(self) -> (int, List[str], List[str]):
        if not self.attended_classes:
            return 0, [], []

        keywords_to_check = self._get_keywords_from_interest()
        
        matched_classes = []
        unmatched_classes = []
        
        for class_name in self.attended_classes:
            is_matched = False
            for keyword in keywords_to_check:
                if keyword.lower() in class_name.lower():
                    matched_classes.append(class_name)
                    is_matched = True
                    break 
            
            if not is_matched:
                unmatched_classes.append(class_name)

        total_attended_count = len(self.attended_classes)
        matched_count = len(matched_classes)
        
        score = 0
        if total_attended_count > 0:
            score = int((matched_count / total_attended_count) * 100)
            
        return score, matched_classes, sorted(unmatched_classes)

def get_recommended_url(self) -> List[Dict[str, str]]:
        base_urls = {
            "링커리어": "https://linkareer.com/search?q={}&page=1",
            "위비티": "https://www.wevity.com/?c=find&s=1&keyword={}",
            "씽굿": "https://www.thinkcontest.com/Contest/Search/result.html?page=1&search={}"
        }

        # 2. 현재 관심 분야 키워드 가져오기 (예: "회로", "AI")
        keyword = self.interested
        
        # 3. 관심 분야가 없으면 빈 리스트 반환
        if not keyword:
            return []

        # 4. 결과 리스트 생성
        recommended_links = []
        
        # 각 사이트별로 검색 링크 생성
        for site_name, url_pattern in base_urls.items():
            # 예: "위비티"에서 "회로" 검색하는 URL 만들기
            full_url = url_pattern.format(keyword)
            
            # 리스트에 추가
            recommended_links.append({
                "title": f"{site_name}에서 '{keyword}' 공모전 검색",
                "url": full_url
            })
            
        # 5. (선택) 분야별 특화 사이트가 있다면 추가 (예: AI는 AI Hub)
        if keyword == "AI":
            recommended_links.append({
                "title": "AI Hub (데이터셋 포털)",
                "url": "https://aihub.or.kr/"
            })
        elif keyword == "반도체":
             recommended_links.append({
                "title": "반도체산업협회 (지원사업)",
                "url": "https://www.ksia.or.kr/"
            })

        return recommended_links






