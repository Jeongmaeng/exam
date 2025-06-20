import tkinter as tk
from tkinter import ttk

def open_view_window(parent):
    view_win = tk.Toplevel(parent)
    view_win.title("거래 내역 조회")
    view_win.geometry("800x400")

    # ----------- Treeview 테이블 ----------
    columns = ("날짜", "구분", "금액", "거래처", "비고")

    tree = ttk.Treeview(view_win, columns=columns, show="headings", height=15)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # ----------- 더미 데이터 예시 ----------
    sample_data = [
        ("2025-06-17", "매입", "120000", "ABC상사", "노트북 구매"),
        ("2025-06-17", "매출", "210000", "XYZ기업", "서버 납품"),
        ("2025-06-16", "미수", "50000", "홍길동", "지급 지연")
    ]

    for row in sample_data:
        tree.insert("", "end", values=row)

    # ----------- 닫기 버튼 ----------
    tk.Button(view_win, text="닫기", command=view_win.destroy).pack(pady=10)
