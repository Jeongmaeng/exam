import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def open_input_window(parent):
    input_win = tk.Toplevel(parent)
    input_win.title("거래 입력")
    input_win.geometry("400x350")
    
    # ---------- 항목들 ----------
    tk.Label(input_win, text="날짜 (YYYY-MM-DD):").pack(anchor="w", padx=20, pady=(10, 0))
    entry_date = tk.Entry(input_win)
    entry_date.insert(0, datetime.today().strftime('%Y-%m-%d'))
    entry_date.pack(padx=20, pady=5)

    tk.Label(input_win, text="구분:").pack(anchor="w", padx=20, pady=(10, 0))
    combo_type = ttk.Combobox(input_win, values=["매입", "매출", "미수", "지급"], state="readonly")
    combo_type.set("매입")
    combo_type.pack(padx=20, pady=5)

    tk.Label(input_win, text="금액:").pack(anchor="w", padx=20, pady=(10, 0))
    entry_amount = tk.Entry(input_win)
    entry_amount.pack(padx=20, pady=5)

    tk.Label(input_win, text="거래처:").pack(anchor="w", padx=20, pady=(10, 0))
    entry_partner = tk.Entry(input_win)
    entry_partner.pack(padx=20, pady=5)

    tk.Label(input_win, text="비고:").pack(anchor="w", padx=20, pady=(10, 0))
    entry_note = tk.Entry(input_win)
    entry_note.pack(padx=20, pady=5)

    # ---------- 저장 버튼 ----------
    def save_entry():
        date = entry_date.get()
        type_ = combo_type.get()
        amount = entry_amount.get()
        partner = entry_partner.get()
        note = entry_note.get()

        # 필수 입력 확인
        if not (date and type_ and amount):
            messagebox.showwarning("입력 오류", "날짜, 구분, 금액은 필수 항목입니다.")
            return

        try:
            float(amount)
        except ValueError:
            messagebox.showwarning("입력 오류", "금액은 숫자로 입력해주세요.")
            return

        # 저장 로직은 이후 db_handler 또는 trade_handler.py에 작성 예정
        print(f"[SAVE] {date} | {type_} | {amount} | {partner} | {note}")
        messagebox.showinfo("저장 완료", "데이터가 저장되었습니다.")
        input_win.destroy()

    tk.Button(input_win, text="저장", command=save_entry, width=15).pack(pady=20)
