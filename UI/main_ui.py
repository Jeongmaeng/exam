import tkinter as tk
from input_ui import open_input_window
from view_ui import open_view_window

def open_main_window(username, login_root, reset_fields_func):
    main_win = tk.Toplevel(login_root)
    main_win.title("관리 프로그램")
    main_win.geometry("600x400")

    # ---------- 상단 영역 (Welcome + 로그아웃) ----------
    top_frame = tk.Frame(main_win)
    top_frame.pack(fill="x", pady=10, padx=10)

    tk.Label(top_frame, text=f"Welcome, {username}!", font=("Arial", 14)).pack(side="left")

    def logout():
        main_win.destroy()
        reset_fields_func()
        login_root.deiconify()
        login_root.after(100, lambda: login_root.focus_force())
        login_root.after(150, lambda: login_root.children['!frame'].children['!entry'].focus_set())

    tk.Button(top_frame, text="로그아웃", command=logout).pack(side="right")

    # ---------- 중앙 버튼 영역 ----------
    button_frame = tk.Frame(main_win)
    button_frame.pack(pady=60)

    tk.Button(button_frame, text="입력하기", width=20, height=2, command=lambda: open_input_window(main_win)).pack(pady=10)
    tk.Button(button_frame, text="조회하기", width=20, height=2, command=lambda: open_view_window(main_win)).pack(pady=10)

