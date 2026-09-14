from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Jika sudah login, langsung ke dashboard
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        
        user = User.query.filter_by(email=email).first()
        
        if not user or not user.check_password(password):
            flash('Email atau password salah!', 'danger')
            return redirect(url_for('auth.login'))
        
        # Cek apakah user ini admin
        if user.role != 'admin':
            flash('Anda tidak memiliki akses ke panel admin.', 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=remember)
        flash(f'Selamat datang, {user.nama_lengkap}!', 'success')
        
        # Redirect ke halaman yang diminta sebelumnya, atau ke dashboard
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('admin.dashboard'))
    
    return render_template('admin/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Anda telah logout.', 'info')
    return redirect(url_for('auth.login'))