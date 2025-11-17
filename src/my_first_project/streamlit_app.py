import streamlit as st
from data import prof_list, related_keywords
from main import EEStudent_Info

st.set_page_config(page_title="전자공학 추천 시스템", layout="wide")
st.title("💡 전자공학 수업/연구실 추천 시스템 ")
st.subheader("-전자공학과 학생의 관심도에 맞춘 성공적인 수업 수강과 학부연구를 위한 앱")

st.markdown("내가 관심 있는 분야는 알겠는데... 무슨 수업을 들어야되는거지?")
st.markdown("학연생.. 다들 하니까 하고 싶은데 어떤 교수님 랩실로 들어가야되는거지.. 내가 관심있는 분야랑 관련된 교수님이 계신가?")
st.markdown("이런 고민을 해봤다면? 정답은 **전자공학 추천 시스템**")
@st.cache_resource
def load_student_helper():
    return EEStudent_Info(all_professors=prof_list)

student_helper = load_student_helper()

st.header("1. 당신의 정보를 입력하세요")
year=[1,2,3,4]
col1, col2 = st.columns(2)
with col1:
    school_year = st.radio("학년:", year)
with col2:
    interest_options = list(related_keywords.keys()) + ["AI", "머신러닝", "로봇"]
    interest = st.selectbox(
        "관심 분야를 선택하세요:",
        options=interest_options,
        index=0
    )

st.divider()

st.header("2. 수강한 과목을 모두 선택하세요")

tab_basic, tab_required, tab_select, tab_advanced = st.tabs([
    "🎓 전공기초", "✅ 전공필수", "📚 전공선택 (실험포함)", "🔬 심화과목"
])

all_attended_list = []

with tab_basic:
    select_all_basic = st.checkbox("👉 전공기초 모두 수강", key="cb_basic")
    
    if select_all_basic:
        st.multiselect(
            "수강한 전공기초 과목:",
            options=student_helper.course_basic,
            default=list(student_helper.course_basic),
            disabled=True,
            key="basic"
        )
        all_attended_list.extend(student_helper.course_basic)
    else:
        attended_basic = st.multiselect(
            "수강한 전공기초 과목을 선택하세요:",
            options=student_helper.course_basic,
            key="basic"
        )
        all_attended_list.extend(attended_basic)

with tab_required:
    select_all_required = st.checkbox("👉 전공필수 모두 수강", key="cb_required")
    
    if select_all_required:
        st.multiselect(
            "수강한 전공필수 과목:",
            options=student_helper.course_required,
            default=list(student_helper.course_required),
            disabled=True,
            key="required"
        )
        all_attended_list.extend(student_helper.course_required)
    else:
        attended_required = st.multiselect(
            "수강한 전공필수 과목을 선택하세요:",
            options=student_helper.course_required,
            key="required"
        )
        all_attended_list.extend(attended_required)

with tab_select:
    select_all_select = st.checkbox("👉 전공선택(기본) 모두 수강", key="cb_select")
    if select_all_select:
        st.multiselect(
            "수강한 전공선택 과목:",
            options=student_helper.course_select,
            default=list(student_helper.course_select),
            disabled=True, key="select"
        )
        all_attended_list.extend(student_helper.course_select)
    else:
        attended_select = st.multiselect(
            "수강한 전공선택 과목을 선택하세요:",
            options=student_helper.course_select, key="select"
        )
        all_attended_list.extend(attended_select)

    st.markdown("---")
    
    select_all_exp = st.checkbox("👉 전공선택(실험) 모두 수강", key="cb_exp")
    if select_all_exp:
        st.multiselect(
            "수강한 전공선택_실험 과목:",
            options=student_helper.course_select_experiment,
            default=list(student_helper.course_select_experiment),
            disabled=True, key="select_exp"
        )
        all_attended_list.extend(student_helper.course_select_experiment)
    else:
        attended_exp = st.multiselect(
            "수강한 전공선택_실험 과목을 선택하세요:",
            options=student_helper.course_select_experiment, key="select_exp"
        )
        all_attended_list.extend(attended_exp)

with tab_advanced:
    select_all_adv_circuit = st.checkbox("👉 회로 심화 모두 수강", key="cb_adv_circuit")
    if select_all_adv_circuit:
        st.multiselect(
            "수강한 회로 심화 과목:",
            options=student_helper.course_advanced_circuit,
            default=list(student_helper.course_advanced_circuit),
            disabled=True, key="adv_circuit"
        )
        all_attended_list.extend(student_helper.course_advanced_circuit)
    else:
        attended_circuit = st.multiselect(
            "수강한 회로 심화 과목을 선택하세요:",
            options=student_helper.course_advanced_circuit, key="adv_circuit"
        )
        all_attended_list.extend(attended_circuit)

    st.markdown("---")

    select_all_adv_signal = st.checkbox("👉 신호시스템 심화 모두 수강", key="cb_adv_signal")
    if select_all_adv_signal:
        st.multiselect(
            "수강한 신호시스템 심화 과목:",
            options=student_helper.course_advanced_signalsystem,
            default=list(student_helper.course_advanced_signalsystem),
            disabled=True, key="adv_signal"
        )
        all_attended_list.extend(student_helper.course_advanced_signalsystem)
    else:
        attended_signal = st.multiselect(
            "수강한 신호시스템 심화 과목을 선택하세요:",
            options=student_helper.course_advanced_signalsystem, key="adv_signal"
        )
        all_attended_list.extend(attended_signal)

    st.markdown("---")

    select_all_adv_semi = st.checkbox("👉 반도체 심화 모두 수강", key="cb_adv_semi")
    if select_all_adv_semi:
        st.multiselect(
            "수강한 반도체 심화 과목:",
            options=student_helper.course_advanced_semiconductor,
            default=list(student_helper.course_advanced_semiconductor),
            disabled=True, key="adv_semi"
        )
        all_attended_list.extend(student_helper.course_advanced_semiconductor)
    else:
        attended_semi = st.multiselect(
            "수강한 반도체 심화 과목을 선택하세요:",
            options=student_helper.course_advanced_semiconductor, key="adv_semi"
        )
        all_attended_list.extend(attended_semi)

st.divider()
if st.button("🚀 나에게 맞는 추천 받기!", type="primary", use_container_width=True):
    
    if not interest or not all_attended_list:
        st.error("⚠️ 관심 분야를 입력하고, 수강한 과목을 1개 이상 선택해주세요!")
    else:
        student_helper.get_student_interest(
            school_year=school_year, 
            interested=interest
        )
        
        student_helper.set_attended_classes(all_attended_list)
        
        profs = student_helper.recommend_professors_by_interest()
        remaining_required = student_helper.recommend_remaining_by_category("전공필수")
        all_interest_courses, attended_interest_courses = student_helper.recommend_classes_by_interest()
        final_interest_courses = all_interest_courses - attended_interest_courses
        
        match_score, matched_classes, unmatched_classes = student_helper.analyze_interest_match()
        
        recommended_url = student_helper.get_recommended_url()
                
        st.header(f"'{interest}' 분야에 대한 맞춤 추천 결과입니다.")

        st.subheader(f"📈 '{interest}' 분야 수강 일치율")
        st.metric(
            label="내 관심 분야와 수강한 과목의 일치도",
            value=f"{match_score} %",
            delta=f"총 {len(all_attended_list)}개 중 {len(matched_classes)}개 일치"
        )
        if matched_classes:
            st.success(f"✅ 일치하는 과목: {', '.join(matched_classes)}")
        else:
            st.warning("아직 관심 분야와 직접적으로 일치하는 과목을 수강하지 않았네요.")

        st.divider()
        
        st.subheader("🔗 관련 공모전 정보")
        if recommended_url:
            st.markdown(f"**[{interest} 관련 공모전/활동 보러가기 (Linkareer)]({recommended_url})**")
            st.caption(f"링크: {recommended_url}")
        else:
            st.info(f"'{interest}' 분야에 대한 맞춤 공모전 링크를 찾지 못했습니다.")

        st.divider()

        col_prof, col_course = st.columns(2)
        
        with col_prof:
            st.subheader("👨‍🏫 추천 교수님")
            if profs:
                for prof in profs:
                    st.markdown(f"**{prof.name} 교수님** ({prof.office_location})")
                    st.caption(f"주요 연구: {prof.research}")
            else:
                st.warning("관련 교수님을 찾지 못했습니다.")
        
        with col_course:
            st.subheader(f"🎓 '{interest}' 분야 관련 추천 과목")
            if final_interest_courses:
                for course in sorted(list(final_interest_courses)):
                    st.info(course)
            else:
                if all_interest_courses:
                    st.success("🎉 대단해요! 이 분야의 모든 추천 과목을 이미 수강하셨습니다!")
                else:
                    st.warning("관련 추천 과목을 찾지 못했습니다.")

            if attended_interest_courses:
                st.caption(f"참고: 이미 수강한 관련 과목: {', '.join(sorted(list(attended_interest_courses)))}")

            st.subheader("✅ 남은 전공필수 과목")
            if remaining_required:
                for course in remaining_required:
                    st.error(course)
            else:
                st.success("🎉 축하합니다! 전공필수 과목을 모두 수강하셨습니다!")
