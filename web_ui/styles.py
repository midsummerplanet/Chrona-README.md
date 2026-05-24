from __future__ import annotations

import streamlit as st


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        :root {
            color-scheme: light;
            --ink: #0A2540;
            --ink-2: #083B66;
            --muted: #4f6478;
            --teal: #14B8A6;
            --blue: #3B82F6;
            --violet: #8B5CF6;
            --glass: rgba(255, 255, 255, 0.75);
            --glass-strong: rgba(255, 255, 255, 0.88);
            --line: rgba(20, 184, 166, 0.30);
            --shadow: 0 18px 46px rgba(10, 37, 64, 0.10);
            --shadow-hover: 0 24px 58px rgba(59, 130, 246, 0.16);
            --radius-sm: 12px;
            --radius-md: 16px;
            --radius-lg: 20px;
            --ease: 0.3s ease;
        }

        @keyframes flow-bg {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes gradient-shift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes gradient-border {
            0% { border-color: rgba(20, 184, 166, 0.70); }
            33% { border-color: rgba(59, 130, 246, 0.70); }
            66% { border-color: rgba(139, 92, 246, 0.70); }
            100% { border-color: rgba(20, 184, 166, 0.70); }
        }

        html,
        body {
            background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 25%, #f0f9ff 50%, #faf5ff 75%, #f0fdf4 100%) !important;
        }

        .stApp {
            color: var(--ink);
            background:
                linear-gradient(135deg,
                    rgba(167, 243, 208, 0.70) 0%,
                    rgba(224, 242, 254, 0.65) 25%,
                    rgba(139, 92, 246, 0.12) 50%,
                    rgba(167, 243, 208, 0.55) 75%,
                    rgba(224, 242, 254, 0.60) 100%);
            background-size: 400% 400% !important;
            animation: flow-bg 25s ease infinite;
            position: relative;
        }

        .stApp::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background:
                radial-gradient(circle at 15% 20%, rgba(20, 184, 166, 0.28), transparent 40%),
                radial-gradient(circle at 85% 15%, rgba(59, 130, 246, 0.24), transparent 38%),
                radial-gradient(circle at 50% 80%, rgba(139, 92, 246, 0.18), transparent 35%),
                radial-gradient(circle at 70% 50%, rgba(167, 243, 208, 0.35), transparent 30%);
            pointer-events: none;
            z-index: 0;
            animation: flow-bg 30s ease infinite reverse;
        }

        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > .main {
            color: var(--ink);
            background: transparent !important;
            position: relative;
            z-index: 1;
        }

        [data-testid="stDecoration"],
        [data-testid="stToolbar"],
        [data-testid="stStatusWidget"] {
            color: var(--ink);
            background: rgba(255, 255, 255, 0.50);
        }

        [data-testid="stHeader"] {
            background: rgba(255, 255, 255, 0.30);
        }

        .block-container {
            padding-top: 2.25rem;
            padding-bottom: 12rem;
            max-width: 1180px;
        }

        h1,
        h2,
        h3,
        [data-testid="stMarkdownContainer"] h1,
        [data-testid="stMarkdownContainer"] h2,
        [data-testid="stMarkdownContainer"] h3 {
            color: var(--ink);
            font-weight: 780;
            letter-spacing: 0;
        }

        h1,
        [data-testid="stMarkdownContainer"] h1 {
            background: linear-gradient(110deg, var(--ink), var(--ink-2), var(--teal));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .stCaption,
        [data-testid="stCaptionContainer"],
        p,
        label,
        .stMarkdown {
            color: var(--muted);
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.82) 0%, rgba(240, 253, 244, 0.78) 100%) !important;
            backdrop-filter: blur(16px);
            border-right: 1px solid rgba(20, 184, 166, 0.28);
        }

        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {
            color: var(--ink);
        }

        button,
        [data-testid="stBaseButton-primary"],
        [data-testid="stBaseButton-secondary"],
        button[kind="primary"],
        button[kind="secondary"],
        button[kind="primaryFormSubmit"],
        button[kind="formSubmit"] {
            border-radius: 999px !important;
            border: 1px solid rgba(20, 184, 166, 0.28) !important;
            color: var(--ink) !important;
            background: rgba(255, 255, 255, 0.72) !important;
            box-shadow: 0 10px 26px rgba(10, 37, 64, 0.08);
            font-weight: 700 !important;
            transition: transform var(--ease), box-shadow var(--ease), border-color var(--ease), background var(--ease);
        }

        button:hover,
        [data-testid="stBaseButton-secondary"]:hover {
            transform: translateY(-2px);
            border-color: rgba(59, 130, 246, 0.42) !important;
            box-shadow: var(--shadow-hover);
        }

        [data-testid="stBaseButton-primary"],
        button[kind="primary"],
        button[kind="primaryFormSubmit"],
        .st-key-task_composer button[kind="primaryFormSubmit"],
        .task-edit-shell button[kind="primaryFormSubmit"] {
            border: 0 !important;
            color: white !important;
            background: linear-gradient(120deg, var(--teal), var(--blue), var(--violet)) !important;
            background-size: 220% 220% !important;
            animation: gradient-shift 8s ease infinite;
        }

        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea,
        [data-testid="stSelectbox"] div[data-baseweb="select"] > div,
        [data-testid="stDateInput"] input,
        [data-testid="stTimeInput"] input,
        [data-testid="stNumberInput"] input {
            border-radius: var(--radius-sm) !important;
            border-color: rgba(20, 184, 166, 0.28) !important;
            background: rgba(255, 255, 255, 0.64) !important;
            color: var(--ink) !important;
            transition: border-color var(--ease), box-shadow var(--ease), background var(--ease);
        }

        [data-testid="stTextInput"] input:focus,
        [data-testid="stTextArea"] textarea:focus,
        [data-testid="stDateInput"] input:focus,
        [data-testid="stTimeInput"] input:focus,
        [data-testid="stNumberInput"] input:focus {
            border-color: rgba(59, 130, 246, 0.58) !important;
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.12) !important;
        }

        [data-testid="stMetric"],
        [data-testid="stAlert"],
        [data-testid="stExpander"],
        div[data-testid="stForm"] {
            border-radius: var(--radius-md) !important;
            border: 1px solid var(--line) !important;
            background: var(--glass) !important;
            backdrop-filter: blur(10px);
            box-shadow: 0 14px 36px rgba(10, 37, 64, 0.08);
        }

        [data-testid="stMetric"] {
            padding: 0.75rem 0.9rem;
        }

        [data-testid="stAlert"] {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.90) 0%, rgba(240, 253, 244, 0.75) 100%) padding-box !important;
            border: 2px solid transparent !important;
            border-image: linear-gradient(135deg, var(--teal), var(--blue), var(--violet)) 1 !important;
            border-radius: var(--radius-md) !important;
            backdrop-filter: blur(12px) !important;
        }

        [data-testid="stAlert"] > div {
            color: var(--ink) !important;
        }

        [data-testid="stAlert"] [data-testid="stAlertInner"] {
            color: var(--ink) !important;
        }

        section[data-testid="stSidebar"] [data-testid="stAlert"] {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.92) 0%, rgba(240, 253, 244, 0.80) 100%) padding-box !important;
        }

        div[data-testid="stSuccess"],
        div[data-testid="stWarning"],
        div[data-testid="stError"],
        div[data-testid="stInfo"] {
            border: none !important;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.92) 0%, rgba(240, 253, 244, 0.80) 100%) padding-box !important;
            border-radius: var(--radius-md) !important;
            backdrop-filter: blur(12px) !important;
        }

        div[data-testid="stSuccess"]::before,
        div[data-testid="stWarning"]::before,
        div[data-testid="stError"]::before,
        div[data-testid="stInfo"]::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(135deg, var(--teal), var(--blue), var(--violet));
            border-radius: calc(var(--radius-md) + 2px);
            z-index: -1;
        }

        div[data-testid="stSuccess"],
        div[data-testid="stWarning"],
        div[data-testid="stError"],
        div[data-testid="stInfo"] {
            position: relative;
            z-index: 1;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.75rem;
            border-radius: 999px;
            padding: 0.35rem;
            background: rgba(255, 255, 255, 0.54);
            border: 1px solid rgba(20, 184, 166, 0.18);
            backdrop-filter: blur(10px);
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 999px;
            color: var(--muted);
            font-weight: 700;
            padding: 0.5rem 1.5rem;
            min-width: 120px;
            transition: color var(--ease), background var(--ease);
        }

        .stTabs [aria-selected="true"] {
            color: white;
            background: linear-gradient(120deg, var(--teal), var(--blue));
        }

        .task-list-shell {
            max-width: 980px;
            margin: 1.25rem auto 1.5rem auto;
        }

        .task-list-empty,
        .day-list-empty,
        .calendar-empty {
            min-height: 260px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            border: 1px dashed rgba(20, 184, 166, 0.50);
            border-radius: var(--radius-lg);
            background: linear-gradient(var(--glass), var(--glass)) padding-box,
                        linear-gradient(135deg, rgba(20, 184, 166, 0.20), rgba(59, 130, 246, 0.15), rgba(139, 92, 246, 0.12)) border-box;
            backdrop-filter: blur(12px);
            box-shadow: var(--shadow);
            transition: transform var(--ease), box-shadow var(--ease), border-color var(--ease);
        }

        .task-list-empty:hover,
        .day-list-empty:hover,
        .calendar-empty:hover {
            transform: translateY(-3px);
            border-color: rgba(59, 130, 246, 0.60);
            box-shadow: var(--shadow-hover);
        }

        .task-list-empty-title,
        .day-list-empty-title,
        .profile-memory-title {
            font-size: 1.08rem;
            font-weight: 780;
            background: linear-gradient(110deg, var(--ink), var(--ink-2), var(--teal));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .task-list-empty-copy,
        .day-list-empty-copy {
            margin-top: 0.35rem;
            max-width: 430px;
            color: var(--muted);
            font-size: 0.9rem;
            line-height: 1.5;
        }

        .timeline-shell {
            margin-top: 1rem;
        }

        .day-list-shell {
            display: grid;
            gap: 0.78rem;
            margin-top: 0.75rem;
        }

        .day-list-summary {
            color: var(--ink-2);
            font-size: 0.88rem;
            font-weight: 700;
            padding: 0 0.1rem;
        }

        .day-task-card,
        div[class*="st-key-day_task_card_"],
        div[class*="st-key-unresolved_task_card_"],
        .task-edit-shell,
        .profile-memory-card,
        .schedule-block,
        .st-key-task_composer {
            border: 1px solid rgba(20, 184, 166, 0.35);
            border-radius: var(--radius-md);
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.82) 0%, rgba(240, 253, 244, 0.65) 100%);
            backdrop-filter: blur(12px);
            box-shadow: var(--shadow);
            color: var(--ink);
            box-sizing: border-box;
            transition: transform var(--ease), box-shadow var(--ease), border-color var(--ease), background var(--ease);
        }

        .day-task-card:hover,
        div[class*="st-key-day_task_card_"]:hover,
        div[class*="st-key-unresolved_task_card_"]:hover,
        .task-edit-shell:hover,
        .profile-memory-card:hover,
        .schedule-block:hover,
        .st-key-task_composer:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-hover);
            border-color: rgba(59, 130, 246, 0.50);
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.90) 0%, rgba(240, 253, 244, 0.75) 100%);
        }

        .day-task-card {
            height: 136px;
            margin-top: 0.78rem;
            padding: 0.86rem 1rem;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        div[class*="st-key-day_task_card_"] {
            height: 136px;
            margin-top: 0.78rem;
            padding: 0.72rem 0.85rem;
            overflow: hidden;
        }

        div[class*="st-key-day_task_card_"] [data-testid="stHorizontalBlock"],
        div[class*="st-key-unresolved_task_card_"] [data-testid="stHorizontalBlock"] {
            align-items: stretch;
        }

        div[class*="st-key-day_task_card_"] button,
        div[class*="st-key-unresolved_task_card_"] button {
            min-height: 2.15rem;
        }

        .day-task-time {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.75rem;
            color: var(--ink-2);
            font-size: 0.86rem;
            font-weight: 750;
            font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
        }

        .day-task-time strong {
            color: var(--teal);
            font-size: 0.75rem;
            font-weight: 760;
            white-space: nowrap;
        }

        .day-task-title,
        .unresolved-task-head,
        .schedule-title,
        .calendar-task-title {
            color: var(--ink);
            font-weight: 780;
            letter-spacing: 0;
        }

        .day-task-title {
            font-size: 1.02rem;
            line-height: 1.28;
            overflow-wrap: anywhere;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        .day-task-meta,
        .unresolved-task-meta,
        .schedule-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 0.42rem;
            color: var(--muted);
            font-size: 0.76rem;
            font-weight: 650;
        }

        .day-task-meta span,
        .unresolved-task-meta span,
        .schedule-meta span,
        .unresolved-task-head strong {
            border: 1px solid rgba(20, 184, 166, 0.30);
            border-radius: 999px;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.70) 0%, rgba(240, 253, 244, 0.55) 100%);
            padding: 0.12rem 0.46rem;
            max-width: 100%;
            overflow-wrap: anywhere;
            color: var(--ink-2);
        }

        .day-task-content {
            height: 106px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden;
        }

        .day-task-done-badge {
            border: 1px solid rgba(20, 184, 166, 0.30);
            border-radius: 999px;
            padding: 0.42rem 0.55rem;
            background: rgba(167, 243, 208, 0.62);
            color: #0f766e;
            font-size: 0.82rem;
            font-weight: 780;
            text-align: center;
            white-space: nowrap;
        }

        div[class*="st-key-unresolved_task_card_"] {
            min-height: 112px;
            margin-top: 0.78rem;
            padding: 0.86rem 1rem;
        }

        .unresolved-task-content {
            min-height: 82px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .unresolved-task-head {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 0.75rem;
            font-size: 1rem;
            line-height: 1.28;
        }

        .unresolved-task-head span {
            overflow-wrap: anywhere;
        }

        .unresolved-task-head strong {
            font-size: 0.76rem;
            white-space: nowrap;
        }

        .unresolved-task-meta {
            margin-top: 0.8rem;
        }

        .task-edit-shell {
            margin: 1.05rem 0 1.1rem 0;
            padding: 1rem;
        }

        .task-edit-shell [data-testid="stForm"],
        .st-key-task_composer [data-testid="stForm"] {
            border: 0 !important;
            padding: 0;
            background: transparent !important;
            box-shadow: none;
        }

        .calendar-week-title {
            text-align: center;
            font-weight: 750;
            color: var(--ink);
            padding: 0.45rem 0 0.35rem 0;
            font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
        }

        .calendar-shell {
            margin-top: 0.55rem;
            overflow-x: auto;
            padding-bottom: 0.35rem;
        }

        .calendar-grid {
            min-width: 920px;
            display: grid;
            grid-template-columns: 82px repeat(7, minmax(112px, 1fr));
            border: 1px solid rgba(20, 184, 166, 0.35);
            border-radius: var(--radius-md);
            overflow: hidden;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.85) 0%, rgba(240, 253, 244, 0.70) 100%);
            backdrop-filter: blur(12px);
            box-shadow: var(--shadow);
        }

        .calendar-time-column,
        .calendar-day-column {
            border-right: 1px solid rgba(20, 184, 166, 0.22);
            background: rgba(255, 255, 255, 0.50);
        }

        .calendar-day-column:last-child {
            border-right: 0;
        }

        .calendar-corner,
        .calendar-day-head {
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-bottom: 1px solid rgba(20, 184, 166, 0.25);
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.75) 0%, rgba(240, 253, 244, 0.60) 100%);
            color: var(--ink-2);
            font-size: 0.86rem;
            font-weight: 750;
            box-sizing: border-box;
        }

        .calendar-day-head {
            flex-direction: column;
            gap: 0.08rem;
        }

        .calendar-day-head span {
            color: var(--ink);
        }

        .calendar-day-head strong {
            color: var(--muted);
            font-size: 0.74rem;
            font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
        }

        .calendar-time-body,
        .calendar-day-body {
            position: relative;
        }

        .calendar-day-body {
            background:
                repeating-linear-gradient(
                    to bottom,
                    rgba(20, 184, 166, 0.18) 0,
                    rgba(20, 184, 166, 0.18) 1px,
                    transparent 1px,
                    transparent 46px
                ),
                linear-gradient(135deg, rgba(255, 255, 255, 0.55) 0%, rgba(240, 253, 244, 0.40) 100%);
        }

        .calendar-time-label {
            position: absolute;
            right: 0.7rem;
            color: var(--muted);
            font-size: 0.8rem;
            font-weight: 650;
            font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
            white-space: nowrap;
        }

        .calendar-task-block {
            position: absolute;
            left: 0.44rem;
            right: 0.44rem;
            border-left: 4px solid rgba(20, 184, 166, 0.72);
            border-radius: var(--radius-sm);
            padding: 0.25rem 0.38rem;
            box-shadow: 0 10px 26px rgba(10, 37, 64, 0.10);
            overflow: hidden;
            color: var(--ink);
            backdrop-filter: blur(8px);
            transition: transform var(--ease), box-shadow var(--ease);
        }

        .calendar-task-block:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-hover);
        }

        .profile-memory-card {
            padding: 0.78rem 0.82rem;
            margin: 0.4rem 0 0.8rem 0;
        }

        .profile-memory-card p {
            margin: 0.28rem 0;
            color: var(--muted);
            font-size: 0.84rem;
            line-height: 1.42;
        }

        .calendar-task-time {
            font-size: 0.64rem;
            color: var(--ink-2);
            font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
            white-space: nowrap;
        }

        .calendar-task-title {
            margin-top: 0.08rem;
            font-size: 0.76rem;
            line-height: 1.22;
            overflow-wrap: anywhere;
        }

        .calendar-task-meta {
            margin-top: 0.12rem;
            font-size: 0.63rem;
            color: var(--muted);
            line-height: 1.2;
            overflow-wrap: anywhere;
        }

        .schedule-block {
            border-left-width: 6px;
            padding: 1rem 1.05rem;
            margin: 0 0 0.9rem 0;
        }

        .schedule-head {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            align-items: flex-start;
        }

        .schedule-time {
            color: var(--muted);
            font-size: 0.82rem;
            font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
        }

        .schedule-title {
            font-size: 1.05rem;
            margin-top: 0.2rem;
            line-height: 1.35;
        }

        .priority-badge {
            color: white;
            border-radius: 999px;
            padding: 0.28rem 0.68rem;
            font-size: 0.78rem;
            font-weight: 750;
            white-space: nowrap;
            font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
            box-shadow: 0 10px 26px rgba(59, 130, 246, 0.22);
        }

        .schedule-meta {
            margin: 0.75rem 0;
        }

        .dimension-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.8rem;
            margin: 0.55rem 0 0.7rem 0;
        }

        .dimension-label {
            font-size: 0.78rem;
            color: var(--muted);
            margin-bottom: 0.24rem;
            font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
        }

        .bar {
            height: 8px;
            border-radius: 999px;
            overflow: hidden;
            background: rgba(20, 184, 166, 0.14);
        }

        .bar span {
            display: block;
            height: 100%;
            border-radius: 999px;
        }

        .reason {
            color: var(--muted);
            font-size: 0.82rem;
            font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
        }

        .st-key-task_composer {
            position: relative;
            width: 100%;
            margin: 1.05rem 0 2rem 0;
            padding: 0.95rem 1rem 0.9rem 1rem;
        }

        .st-key-task_composer .composer-greeting {
            color: var(--ink);
            font-size: 1rem;
            font-weight: 780;
            line-height: 1.25;
            margin: 0 0 0.42rem 0.05rem;
        }

        .st-key-task_composer textarea {
            min-height: 88px !important;
            border-radius: var(--radius-sm);
            border-color: rgba(20, 184, 166, 0.28);
            background: rgba(255, 255, 255, 0.58);
            color: var(--ink);
            font-size: 0.9rem;
            line-height: 1.45;
        }

        .st-key-task_composer textarea::placeholder {
            color: var(--muted);
            font-size: 0.84rem;
            font-weight: 500;
            line-height: 1.45;
        }

        @media (max-width: 760px) {
            .calendar-grid {
                min-width: 820px;
                grid-template-columns: 74px repeat(7, minmax(104px, 1fr));
            }
            .st-key-task_composer {
                padding: 0.78rem;
            }
            .day-task-card {
                height: 148px;
                padding: 0.78rem;
            }
            div[class*="st-key-day_task_card_"] {
                height: 156px;
                padding: 0.68rem;
            }
            .day-task-content {
                height: 126px;
            }
            .day-task-time {
                align-items: flex-start;
                flex-direction: column;
                gap: 0.2rem;
            }
            .schedule-head {
                display: block;
            }
            .priority-badge {
                display: inline-block;
                margin-top: 0.65rem;
            }
            .dimension-grid {
                grid-template-columns: 1fr;
            }
        }

        .styled-alert {
            padding: 0.85rem 1rem;
            border-radius: var(--radius-md);
            margin: 0.5rem 0;
            font-size: 0.9rem;
            line-height: 1.5;
            position: relative;
            backdrop-filter: blur(12px);
        }

        .styled-alert::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: var(--radius-md);
            background: linear-gradient(135deg, var(--teal), var(--blue), var(--violet));
            z-index: -1;
            padding: 2px;
        }

        .styled-alert::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: var(--radius-md);
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(240, 253, 244, 0.85) 100%);
            z-index: -1;
        }

        .styled-alert > *:last-child {
            margin-bottom: 0;
        }

        .styled-alert-warning,
        .styled-alert-error {
            color: var(--ink);
        }

        .styled-alert-success {
            color: var(--ink);
        }

        .styled-alert-info {
            color: var(--ink);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def styled_alert(message: str, alert_type: str = "info") -> None:
    st.markdown(
        f"""
        <div class="styled-alert styled-alert-{alert_type}">
            {message}
        </div>
        """,
        unsafe_allow_html=True,
    )


def styled_warning(message: str) -> None:
    styled_alert(message, "warning")


def styled_error(message: str) -> None:
    styled_alert(message, "error")


def styled_success(message: str) -> None:
    styled_alert(message, "success")


def styled_info(message: str) -> None:
    styled_alert(message, "info")
