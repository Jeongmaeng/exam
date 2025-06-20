import tkinter as tk
from tkinter import messagebox
from db_handler import verify_login, init_admin_account
from main_ui import open_main_window
from view_ui import open_view_window

def login_window():
    def try_login():
        user_id = entry_id.get()
        password = entry_pw.get()
        if verify_login(user_id, password):
            messagebox.showinfo("Success", f"Welcome, {user_id}!")
            #login_win.destroy()
            def reset_fields():
                entry_id.delete(0, tk.END)
                entry_pw.delete(0, tk.END)
                entry_id.focus_set()
            open_main_window(user_id, login_win, reset_fields)  # ✅ 메인창 열기 (Toplevel로)
            login_win.withdraw()  # 로그인 창 숨기기 (원하면 destroy로 완전 종료)
        else:
            messagebox.showerror("Failed", "Invalid ID or password.")

    def close_app():
        login_win.destroy()

    login_win = tk.Tk()
    login_win.title("Login")
    login_win.resizable(False, False)

    # --------- 타이틀 ---------
    title_login = tk.Label(login_win, text= "Login", font=("Arial", 20))
    title_login.pack(pady=(10,15))
    
    # --------- ID 입력 행 ---------
    id_row = tk.Frame(login_win)
    id_row.pack(pady=5, padx=20, anchor="w")
    tk.Label(id_row, text="User ID :", width=10, anchor="e").pack(side="left")
    entry_id = tk.Entry(id_row, width=25)
    entry_id.pack(side="left")
    entry_id.focus_set()

    # --------- PW 입력 행 ---------
    pw_row = tk.Frame(login_win)
    pw_row.pack(pady=5, padx=20, anchor="w")
    tk.Label(pw_row, text="Password :", width=10, anchor="e").pack(side="left")
    entry_pw = tk.Entry(pw_row, show="*", width=25)
    entry_pw.pack(side="left")

    # --------- 버튼 영역 ---------
    frame_buttons = tk.Frame(login_win)
    frame_buttons.pack(pady=(15, 15))

    btn_login = tk.Button(frame_buttons, text="로그인", width=10, command=try_login)
    btn_login.pack(side="left", padx=10)

    btn_exit = tk.Button(frame_buttons, text="나가기", width=10, command=close_app)
    btn_exit.pack(side="right", padx=10)

    login_win.bind('<Return>', lambda event: try_login())
    
    login_win.update_idletasks()
    login_win.geometry("")  # 내부 크기 자동 반영

    login_win.mainloop()

# ---------- 실행 ----------
if __name__ == "__main__":
    init_admin_account()
    login_window()
