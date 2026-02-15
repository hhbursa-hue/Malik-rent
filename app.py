<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Malik - Property Management System</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <style>
        :root {
            --deep-navy: #0A1929;
            --gold: #D4AF37;
            --slate-grey: #64748B;
            --light-gold: #F4E4C1;
            --dark-gold: #B8941E;
            --success: #10B981;
            --warning: #F59E0B;
            --danger: #EF4444;
            --info: #3B82F6;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'IBM Plex Sans Arabic', sans-serif;
            background: linear-gradient(135deg, #0A1929 0%, #1E293B 100%);
            color: white;
            min-height: 100vh;
            overflow-x: hidden;
        }

        /* Login Screen */
        .login-container {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 2rem;
        }

        .login-card {
            background: linear-gradient(145deg, #1E293B 0%, #0F172A 100%);
            border: 2px solid var(--gold);
            border-radius: 20px;
            padding: 3rem;
            max-width: 450px;
            width: 100%;
            box-shadow: 0 25px 50px -12px rgba(212, 175, 55, 0.25);
            text-align: center;
            animation: fadeIn 0.5s ease-in;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .logo-text {
            font-family: 'Playfair Display', serif;
            font-size: 3.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--gold) 0%, var(--light-gold) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
            text-shadow: 0 0 30px rgba(212, 175, 55, 0.3);
        }

        .logo-subtitle {
            font-size: 1.2rem;
            color: var(--slate-grey);
            margin-bottom: 2rem;
        }

        .input-group {
            margin-bottom: 1.5rem;
            text-align: right;
        }

        .input-group label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--light-gold);
            font-weight: 600;
        }

        .input-group input {
            width: 100%;
            padding: 0.75rem 1rem;
            border: 2px solid var(--slate-grey);
            border-radius: 8px;
            background: rgba(30, 41, 59, 0.5);
            color: white;
            font-size: 1rem;
            font-family: 'IBM Plex Sans Arabic', sans-serif;
            transition: all 0.3s ease;
        }

        .input-group input:focus {
            outline: none;
            border-color: var(--gold);
            box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.1);
        }

        .btn-primary {
            width: 100%;
            padding: 0.75rem 2rem;
            background: linear-gradient(135deg, var(--gold) 0%, var(--dark-gold) 100%);
            color: var(--deep-navy);
            border: none;
            border-radius: 8px;
            font-weight: 700;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(212, 175, 55, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(212, 175, 55, 0.5);
        }

        .error-message {
            color: var(--danger);
            margin-top: 1rem;
            padding: 0.75rem;
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid var(--danger);
            border-radius: 8px;
            display: none;
        }

        /* Main App Layout */
        .app-container {
            display: none;
        }

        .app-container.active {
            display: flex;
        }

        .sidebar {
            width: 280px;
            background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
            border-right: 2px solid var(--gold);
            padding: 2rem 1rem;
            position: fixed;
            height: 100vh;
            overflow-y: auto;
            z-index: 100;
        }

        .sidebar-logo {
            text-align: center;
            padding-bottom: 2rem;
            border-bottom: 1px solid var(--slate-grey);
            margin-bottom: 2rem;
        }

        .sidebar-logo-text {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--gold) 0%, var(--light-gold) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .sidebar-logo-subtitle {
            color: var(--slate-grey);
            font-size: 0.875rem;
            margin-top: 0.5rem;
        }

        .nav-btn {
            width: 100%;
            padding: 1rem;
            margin-bottom: 0.75rem;
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid var(--slate-grey);
            border-radius: 8px;
            color: white;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: right;
            font-family: 'IBM Plex Sans Arabic', sans-serif;
        }

        .nav-btn:hover {
            background: rgba(212, 175, 55, 0.1);
            border-color: var(--gold);
        }

        .nav-btn.active {
            background: linear-gradient(135deg, var(--gold) 0%, var(--dark-gold) 100%);
            color: var(--deep-navy);
            border-color: var(--gold);
        }

        .main-content {
            margin-right: 280px;
            padding: 2rem;
            min-height: 100vh;
        }

        .page-title {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            color: var(--gold);
            text-align: center;
            margin-bottom: 3rem;
        }

        /* Property Cards */
        .properties-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .property-card {
            background: linear-gradient(145deg, #1E293B 0%, #0F172A 100%);
            border: 2px solid var(--gold);
            border-radius: 16px;
            overflow: hidden;
            transition: all 0.3s ease;
            cursor: pointer;
            box-shadow: 0 10px 30px -10px rgba(212, 175, 55, 0.2);
            animation: slideIn 0.5s ease-out;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .property-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px -10px rgba(212, 175, 55, 0.4);
            border-color: var(--light-gold);
        }

        .property-image {
            width: 100%;
            height: 200px;
            background: linear-gradient(135deg, #334155 0%, #1E293B 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--gold);
            font-size: 4rem;
            border-bottom: 2px solid var(--gold);
        }

        .property-content {
            padding: 1.5rem;
        }

        .property-name {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--gold);
            margin-bottom: 0.5rem;
        }

        .property-location {
            color: var(--slate-grey);
            font-size: 1rem;
            margin-bottom: 1rem;
        }

        .occupancy-bar {
            background: rgba(100, 116, 139, 0.3);
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 0.5rem;
        }

        .occupancy-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--gold) 0%, var(--light-gold) 100%);
            transition: width 0.5s ease;
        }

        .occupancy-text {
            color: var(--light-gold);
            font-size: 0.875rem;
            font-weight: 600;
            text-align: right;
        }

        /* Units Grid */
        .units-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 1.5rem;
        }

        .unit-card {
            background: linear-gradient(145deg, #1E293B 0%, #0F172A 100%);
            border: 2px solid;
            border-radius: 12px;
            padding: 1.5rem;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
            animation: slideIn 0.5s ease-out;
        }

        .unit-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--gold) 0%, var(--light-gold) 100%);
        }

        .unit-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px -10px rgba(212, 175, 55, 0.3);
        }

        .unit-card.status-active {
            border-color: var(--success);
        }

        .unit-card.status-available {
            border-color: var(--info);
        }

        .unit-card.status-maintenance {
            border-color: var(--danger);
        }

        .unit-card.status-eviction {
            border-color: var(--warning);
        }

        .status-badge {
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.875rem;
            margin-bottom: 1rem;
        }

        .status-badge.active {
            background: rgba(16, 185, 129, 0.2);
            color: var(--success);
            border: 1px solid var(--success);
        }

        .status-badge.available {
            background: rgba(59, 130, 246, 0.2);
            color: var(--info);
            border: 1px solid var(--info);
        }

        .status-badge.maintenance {
            background: rgba(239, 68, 68, 0.2);
            color: var(--danger);
            border: 1px solid var(--danger);
        }

        .status-badge.eviction {
            background: rgba(245, 158, 11, 0.2);
            color: var(--warning);
            border: 1px solid var(--warning);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.6; }
        }

        .unit-number {
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--gold);
            margin-bottom: 0.5rem;
        }

        .unit-details {
            color: #CBD5E1;
            margin-bottom: 0.5rem;
        }

        .tenant-name {
            color: #E2E8F0;
            margin-bottom: 0.5rem;
        }

        .countdown {
            font-size: 0.875rem;
            color: var(--slate-grey);
        }

        .price-tag {
            font-size: 1.75rem;
            font-weight: 700;
            color: var(--gold);
            margin: 0.5rem 0;
        }

        .action-buttons {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin-top: 1rem;
        }

        .action-btn {
            flex: 1;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            border: 1px solid var(--gold);
            background: rgba(212, 175, 55, 0.1);
            color: var(--gold);
            font-size: 0.875rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .action-btn:hover {
            background: var(--gold);
            color: var(--deep-navy);
        }

        /* Financial Widget */
        .financial-health {
            background: linear-gradient(145deg, #1E293B 0%, #0F172A 100%);
            border: 3px solid var(--gold);
            border-radius: 16px;
            padding: 2rem;
            text-align: center;
            box-shadow: 0 20px 40px -10px rgba(212, 175, 55, 0.3);
            margin-bottom: 2rem;
        }

        .financial-label {
            font-size: 1rem;
            color: var(--slate-grey);
            margin-bottom: 0.5rem;
            font-weight: 600;
        }

        .financial-amount {
            font-family: 'Playfair Display', serif;
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--success) 0%, #34D399 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-bottom: 3rem;
        }

        .metric-card {
            background: linear-gradient(145deg, #1E293B 0%, #0F172A 100%);
            border: 2px solid var(--slate-grey);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
        }

        .metric-label {
            color: var(--slate-grey);
            font-size: 0.875rem;
            margin-bottom: 0.5rem;
        }

        .metric-value {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            font-weight: 700;
            color: var(--gold);
        }

        .metric-delta {
            font-size: 0.875rem;
            margin-top: 0.5rem;
        }

        .metric-delta.positive {
            color: var(--success);
        }

        .metric-delta.negative {
            color: var(--danger);
        }

        /* Payment Items */
        .payment-item {
            background: linear-gradient(145deg, #1E293B 0%, #0F172A 100%);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            border: 2px solid transparent;
            transition: all 0.2s ease;
        }

        .payment-item:hover {
            border-color: var(--gold);
        }

        .payment-status-icon {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.25rem;
            flex-shrink: 0;
        }

        .payment-status-icon.paid {
            background: rgba(16, 185, 129, 0.2);
            color: var(--success);
        }

        .payment-status-icon.late {
            background: rgba(239, 68, 68, 0.2);
            color: var(--danger);
            animation: flash 1.5s infinite;
        }

        @keyframes flash {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.4; }
        }

        .payment-details {
            flex: 1;
        }

        .payment-name {
            color: #E2E8F0;
            font-weight: 600;
            margin-bottom: 0.25rem;
        }

        .payment-amount {
            color: var(--gold);
            font-weight: 700;
        }

        .days-overdue {
            color: var(--danger);
            font-size: 0.875rem;
            margin-top: 0.25rem;
        }

        /* Expense Cards */
        .expense-card {
            background: linear-gradient(145deg, #1E293B 0%, #0F172A 100%);
            border: 2px solid var(--slate-grey);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1rem;
        }

        .expense-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .expense-name {
            color: #E2E8F0;
            font-weight: 600;
        }

        .expense-amount {
            color: var(--danger);
            font-weight: 700;
            font-size: 1.125rem;
        }

        /* Charts */
        .charts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .chart-container {
            background: linear-gradient(145deg, #1E293B 0%, #0F172A 100%);
            border: 2px solid var(--slate-grey);
            border-radius: 12px;
            padding: 1.5rem;
        }

        /* Modal */
        .modal-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(10, 25, 41, 0.95);
            align-items: center;
            justify-content: center;
            z-index: 1000;
            padding: 2rem;
        }

        .modal-overlay.active {
            display: flex;
        }

        .modal-content {
            background: linear-gradient(145deg, #1E293B 0%, #0F172A 100%);
            border: 3px solid var(--gold);
            border-radius: 16px;
            padding: 2rem;
            max-width: 600px;
            width: 100%;
            max-height: 80vh;
            overflow-y: auto;
            box-shadow: 0 25px 50px -12px rgba(212, 175, 55, 0.5);
            animation: modalSlideIn 0.3s ease-out;
        }

        @keyframes modalSlideIn {
            from {
                opacity: 0;
                transform: translateY(-50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .modal-header {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: var(--gold);
            margin-bottom: 1.5rem;
            text-align: center;
        }

        .legal-notice {
            background: rgba(239, 68, 68, 0.1);
            border: 2px solid var(--danger);
            border-radius: 8px;
            padding: 1.5rem;
            color: #E2E8F0;
            font-size: 1rem;
            line-height: 1.8;
            text-align: right;
            margin-bottom: 1.5rem;
        }

        .legal-notice p {
            margin-bottom: 1rem;
        }

        .legal-notice strong {
            color: var(--gold);
        }

        .back-btn {
            padding: 0.75rem 2rem;
            background: rgba(212, 175, 55, 0.1);
            border: 2px solid var(--gold);
            border-radius: 8px;
            color: var(--gold);
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-bottom: 2rem;
        }

        .back-btn:hover {
            background: var(--gold);
            color: var(--deep-navy);
        }

        .hidden {
            display: none !important;
        }

        @media (max-width: 768px) {
            .sidebar {
                width: 100%;
                position: relative;
                height: auto;
            }

            .main-content {
                margin-right: 0;
                padding: 1rem;
            }

            .properties-grid,
            .units-grid {
                grid-template-columns: 1fr;
            }

            .charts-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Login Screen -->
    <div id="loginScreen" class="login-container">
        <div class="login-card">
            <div class="logo-text">MALIK</div>
            <div class="logo-subtitle">نظام إدارة العقارات الاحترافي</div>
            
            <div class="input-group">
                <label for="username">اسم المستخدم</label>
                <input type="text" id="username" placeholder="admin">
            </div>
            
            <div class="input-group">
                <label for="password">كلمة المرور</label>
                <input type="password" id="password" placeholder="admin">
            </div>
            
            <button class="btn-primary" onclick="login()">تسجيل الدخول</button>
            
            <div id="loginError" class="error-message">
                اسم المستخدم أو كلمة المرور غير صحيحة
            </div>
        </div>
    </div>

    <!-- Main App -->
    <div id="mainApp" class="app-container">
        <!-- Sidebar -->
        <div class="sidebar">
            <div class="sidebar-logo">
                <div class="sidebar-logo-text">MALIK</div>
                <div class="sidebar-logo-subtitle">نظام إدارة العقارات</div>
            </div>
            
            <button class="nav-btn active" onclick="showView('portfolio')">
                🏠 محفظة العقارات
            </button>
            <button class="nav-btn" onclick="showView('finance')">
                💰 التحكم المالي
            </button>
            <button class="nav-btn" onclick="showView('expenses')">
                🔧 المصروفات والصيانة
            </button>
            
            <div style="margin-top: 2rem; padding-top: 2rem; border-top: 1px solid var(--slate-grey);">
                <button class="nav-btn" onclick="logout()">
                    🚪 تسجيل الخروج
                </button>
            </div>
        </div>

        <!-- Main Content -->
        <div class="main-content">
            <!-- Portfolio View -->
            <div id="portfolioView" class="view-content">
                <h1 class="page-title">محفظة العقارات</h1>
                <div class="properties-grid" id="propertiesGrid"></div>
            </div>

            <!-- Units View -->
            <div id="unitsView" class="view-content hidden">
                <button class="back-btn" onclick="backToPortfolio()">⬅️ العودة</button>
                <h1 class="page-title" id="unitsTitle"></h1>
                <div class="units-grid" id="unitsGrid"></div>
            </div>

            <!-- Finance View -->
            <div id="financeView" class="view-content hidden">
                <h1 class="page-title">لوحة التحكم المالية</h1>
                
                <div class="financial-health">
                    <div class="financial-label">صافي الربح الشهري</div>
                    <div class="financial-amount" id="netProfit"></div>
                </div>

                <div class="metrics-grid">
                    <div class="metric-card">
                        <div class="metric-label">إجمالي المحصل</div>
                        <div class="metric-value" id="totalCollected"></div>
                        <div class="metric-delta positive">▲ 12%</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-label">متأخرات</div>
                        <div class="metric-value" id="totalOverdue"></div>
                        <div class="metric-delta negative">▼ 90 يوم</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-label">المصروفات</div>
                        <div class="metric-value" id="totalExpenses"></div>
                        <div class="metric-delta negative">▼ 5%</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-label">معدل الإشغال</div>
                        <div class="metric-value">83%</div>
                        <div class="metric-delta positive">▲ 5%</div>
                    </div>
                </div>

                <h2 style="color: var(--gold); margin-bottom: 1.5rem; text-align: right;">حالة التحصيل</h2>
                <div id="paymentsGrid"></div>

                <h2 style="color: var(--gold); margin: 3rem 0 1.5rem; text-align: right;">التحليل المالي</h2>
                <div class="charts-grid">
                    <div class="chart-container">
                        <div id="revenueExpenseChart"></div>
                    </div>
                    <div class="chart-container">
                        <div id="expenseBreakdownChart"></div>
                    </div>
                </div>
            </div>

            <!-- Expenses View -->
            <div id="expensesView" class="view-content hidden">
                <h1 class="page-title">تتبع المصروفات والصيانة</h1>
                
                <div class="financial-health">
                    <div class="financial-label">إجمالي المصروفات الشهرية</div>
                    <div class="financial-amount" style="background: linear-gradient(135deg, #EF4444 0%, #F87171 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;" id="totalExpensesDetail"></div>
                </div>

                <div id="expensesGrid"></div>

                <h2 style="color: var(--gold); margin: 3rem 0 1.5rem; text-align: right;">اتجاه المصروفات (آخر 6 أشهر)</h2>
                <div class="chart-container">
                    <div id="expensesTrendChart"></div>
                </div>
            </div>
        </div>
    </div>

    <!-- Legal Notice Modal -->
    <div id="legalModal" class="modal-overlay">
        <div class="modal-content">
            <div class="modal-header">إنذار قانوني رسمي</div>
            <div class="legal-notice" id="legalNoticeContent"></div>
            <button class="btn-primary" onclick="closeLegalModal()">إغلاق</button>
            <button class="btn-primary" onclick="exportPDF()" style="margin-top: 0.5rem;">تصدير كملف PDF</button>
        </div>
    </div>

    <script>
        // Data
        const properties = [
            {
                id: 1,
                name: "برج النخيل",
                location: "الكويت، الصالحية",
                totalUnits: 20,
                occupiedUnits: 16,
                icon: "🏢"
            },
            {
                id: 2,
                name: "مجمع الريان السكني",
                location: "الرياض، العليا",
                totalUnits: 30,
                occupiedUnits: 25,
                icon: "🏘️"
            },
            {
                id: 3,
                name: "أبراج الجوهرة",
                location: "دبي، مركز دبي المالي",
                totalUnits: 15,
                occupiedUnits: 12,
                icon: "🌆"
            }
        ];

        const units = {
            1: [
                {
                    unitNumber: "شقة 101",
                    status: "active",
                    tenant: "أحمد محمد الخالدي",
                    rent: 850,
                    daysRemaining: 45,
                    type: "2 غرف نوم"
                },
                {
                    unitNumber: "شقة 102",
                    status: "available",
                    rent: 900,
                    type: "3 غرف نوم"
                },
                {
                    unitNumber: "شقة 103",
                    status: "active",
                    tenant: "فاطمة سعيد العتيبي",
                    rent: 800,
                    daysRemaining: 120,
                    type: "2 غرف نوم"
                },
                {
                    unitNumber: "شقة 104",
                    status: "maintenance",
                    repairCost: 1200,
                    issue: "تسرب مياه + صيانة التكييف",
                    type: "3 غرف نوم"
                },
                {
                    unitNumber: "شقة 201",
                    status: "active",
                    tenant: "خالد عبدالله السالم",
                    rent: 950,
                    daysRemaining: 200,
                    type: "3 غرف نوم"
                },
                {
                    unitNumber: "شقة 202",
                    status: "eviction",
                    tenant: "محمد علي الدوسري",
                    rent: 850,
                    daysOverdue: 90,
                    type: "2 غرف نوم"
                }
            ],
            2: [
                {
                    unitNumber: "فيلا A1",
                    status: "active",
                    tenant: "عبدالرحمن سليمان المطيري",
                    rent: 2500,
                    daysRemaining: 180,
                    type: "فيلا 5 غرف"
                },
                {
                    unitNumber: "فيلا A2",
                    status: "available",
                    rent: 2800,
                    type: "فيلا 6 غرف"
                },
                {
                    unitNumber: "فيلا B1",
                    status: "active",
                    tenant: "نورة حسن القحطاني",
                    rent: 2400,
                    daysRemaining: 90,
                    type: "فيلا 5 غرف"
                },
                {
                    unitNumber: "فيلا B2",
                    status: "maintenance",
                    repairCost: 3500,
                    issue: "تجديد المطبخ والحمامات",
                    type: "فيلا 6 غرف"
                }
            ],
            3: [
                {
                    unitNumber: "بنتهاوس 3001",
                    status: "active",
                    tenant: "يوسف أحمد البكر",
                    rent: 5000,
                    daysRemaining: 300,
                    type: "بنتهاوس فاخر"
                },
                {
                    unitNumber: "شقة 2801",
                    status: "available",
                    rent: 3500,
                    type: "4 غرف نوم"
                },
                {
                    unitNumber: "شقة 2802",
                    status: "active",
                    tenant: "سارة محمد الشمري",
                    rent: 3200,
                    daysRemaining: 60,
                    type: "3 غرف نوم"
                }
            ]
        };

        const payments = [
            { tenant: "أحمد محمد الخالدي", amount: 850, status: "paid", property: "برج النخيل" },
            { tenant: "فاطمة سعيد العتيبي", amount: 800, status: "paid", property: "برج النخيل" },
            { tenant: "محمد علي الدوسري", amount: 850, status: "late", daysOverdue: 90, property: "برج النخيل" },
            { tenant: "خالد عبدالله السالم", amount: 950, status: "paid", property: "برج النخيل" },
            { tenant: "عبدالرحمن سليمان المطيري", amount: 2500, status: "paid", property: "مجمع الريان السكني" },
            { tenant: "نورة حسن القحطاني", amount: 2400, status: "late", daysOverdue: 15, property: "مجمع الريان السكني" },
            { tenant: "يوسف أحمد البكر", amount: 5000, status: "paid", property: "أبراج الجوهرة" },
            { tenant: "سارة محمد الشمري", amount: 3200, status: "paid", property: "أبراج الجوهرة" }
        ];

        const expenses = [
            { name: "الأمن والحراسة", amount: 3500 },
            { name: "صيانة المصاعد", amount: 1800 },
            { name: "الكهرباء والمياه", amount: 2200 },
            { name: "النظافة", amount: 1500 },
            { name: "الصيانة العامة", amount: 2800 },
            { name: "التأمين", amount: 1200 }
        ];

        let selectedProperty = null;

        // Login
        function login() {
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            
            if (username === 'admin' && password === 'admin') {
                document.getElementById('loginScreen').style.display = 'none';
                document.getElementById('mainApp').classList.add('active');
                renderProperties();
            } else {
                document.getElementById('loginError').style.display = 'block';
            }
        }

        // Logout
        function logout() {
            document.getElementById('mainApp').classList.remove('active');
            document.getElementById('loginScreen').style.display = 'flex';
            document.getElementById('username').value = '';
            document.getElementById('password').value = '';
            document.getElementById('loginError').style.display = 'none';
        }

        // Render Properties
        function renderProperties() {
            const grid = document.getElementById('propertiesGrid');
            grid.innerHTML = '';
            
            properties.forEach(property => {
                const occupancyRate = (property.occupiedUnits / property.totalUnits) * 100;
                
                const card = document.createElement('div');
                card.className = 'property-card';
                card.onclick = () => showUnits(property.id);
                
                card.innerHTML = `
                    <div class="property-image">${property.icon}</div>
                    <div class="property-content">
                        <div class="property-name">${property.name}</div>
                        <div class="property-location">📍 ${property.location}</div>
                        <div class="occupancy-bar">
                            <div class="occupancy-fill" style="width: ${occupancyRate}%"></div>
                        </div>
                        <div class="occupancy-text">
                            ${property.occupiedUnits} / ${property.totalUnits} وحدات مشغولة (${occupancyRate.toFixed(0)}%)
                        </div>
                    </div>
                `;
                
                grid.appendChild(card);
            });
        }

        // Show Units
        function showUnits(propertyId) {
            selectedProperty = propertyId;
            const property = properties.find(p => p.id === propertyId);
            
            document.getElementById('portfolioView').classList.add('hidden');
            document.getElementById('unitsView').classList.remove('hidden');
            document.getElementById('unitsTitle').textContent = `${property.name} - ${property.location}`;
            
            const grid = document.getElementById('unitsGrid');
            grid.innerHTML = '';
            
            units[propertyId].forEach((unit, index) => {
                const card = document.createElement('div');
                card.className = `unit-card status-${unit.status}`;
                
                const statusLabels = {
                    active: 'مؤجرة',
                    available: 'متاحة للتأجير',
                    maintenance: 'تحت الصيانة',
                    eviction: 'إخلاء قانوني'
                };
                
                let content = `
                    <div class="status-badge ${unit.status}">${statusLabels[unit.status]}</div>
                    <div class="unit-number">${unit.unitNumber}</div>
                    <div class="unit-details">${unit.type}</div>
                `;
                
                if (unit.status === 'active') {
                    content += `
                        <div class="tenant-name">المستأجر: ${unit.tenant}</div>
                        <div class="countdown">⏰ ينتهي العقد خلال ${unit.daysRemaining} يوم</div>
                        <div class="price-tag">${unit.rent} د.ك / شهرياً</div>
                    `;
                } else if (unit.status === 'available') {
                    content += `
                        <div style="text-align: center; padding: 1rem 0;">
                            <div style="font-size: 1.25rem; color: var(--info); margin-bottom: 0.5rem;">
                                ✅ جاهزة للتأجير الآن
                            </div>
                            <div class="price-tag">${unit.rent} د.ك / شهرياً</div>
                        </div>
                    `;
                } else if (unit.status === 'maintenance') {
                    content += `
                        <div class="tenant-name">🔧 ${unit.issue}</div>
                        <div class="price-tag" style="color: var(--danger);">
                            تكلفة الإصلاح: ${unit.repairCost} د.ك
                        </div>
                    `;
                } else if (unit.status === 'eviction') {
                    content += `
                        <div class="tenant-name">⚠️ المستأجر: ${unit.tenant}</div>
                        <div class="days-overdue" style="font-size: 1rem; margin-top: 0.5rem;">
                            🚨 متأخر ${unit.daysOverdue} يوم
                        </div>
                        <div class="price-tag">${unit.rent} د.ك / شهرياً</div>
                    `;
                }
                
                content += `
                    <div class="action-buttons">
                        <button class="action-btn">📄 العقد</button>
                        <button class="action-btn">✏️ تعديل</button>
                        ${unit.status === 'eviction' ? 
                            `<button class="action-btn" onclick="showLegalNotice(${index})">⚖️ إنذار</button>` : 
                            `<button class="action-btn">🔧 صيانة</button>`
                        }
                    </div>
                `;
                
                card.innerHTML = content;
                grid.appendChild(card);
            });
        }

        // Back to Portfolio
        function backToPortfolio() {
            document.getElementById('unitsView').classList.add('hidden');
            document.getElementById('portfolioView').classList.remove('hidden');
            selectedProperty = null;
        }

        // Show Legal Notice
        function showLegalNotice(unitIndex) {
            const unit = units[selectedProperty][unitIndex];
            const today = new Date().toLocaleDateString('ar-SA');
            
            const content = `
                <p style="text-align: center; font-weight: 700; font-size: 1.25rem; margin-bottom: 1rem;">
                    إنذار رسمي بالإخلاء
                </p>
                
                <p>بسم الله الرحمن الرحيم</p>
                
                <p><strong>إلى المستأجر:</strong> ${unit.tenant}</p>
                <p><strong>الوحدة:</strong> ${unit.unitNumber}</p>
                
                <p style="margin-top: 1.5rem;">
                نحيطكم علماً بأنكم متأخرون عن سداد الإيجار المستحق عليكم لمدة <strong>${unit.daysOverdue} يوماً</strong>، 
                والبالغ قيمته <strong>${unit.rent} دينار كويتي</strong> شهرياً.
                </p>
                
                <p>
                وعليه، نطالبكم بسداد كامل المبالغ المستحقة خلال <strong>أسبوع واحد (7 أيام)</strong> من تاريخ استلام هذا الإنذار.
                </p>
                
                <p style="margin-top: 1.5rem; padding: 1rem; background: rgba(239, 68, 68, 0.2); border-radius: 8px;">
                <strong>⚠️ تحذير:</strong>
                في حالة عدم السداد خلال المهلة المحددة، سيتم اتخاذ الإجراءات القانونية اللازمة لإخلاء الوحدة 
                وفقاً لأحكام القانون المدني وقانون الإيجارات، مع المطالبة بكامل المستحقات والتعويضات.
                </p>
                
                <p style="margin-top: 1.5rem;">
                <strong>التاريخ:</strong> ${today}<br>
                <strong>التوقيع:</strong> إدارة العقارات - نظام مالك
                </p>
            `;
            
            document.getElementById('legalNoticeContent').innerHTML = content;
            document.getElementById('legalModal').classList.add('active');
        }

        // Close Legal Modal
        function closeLegalModal() {
            document.getElementById('legalModal').classList.remove('active');
        }

        // Export PDF (placeholder)
        function exportPDF() {
            alert('✅ تم تصدير الإنذار القانوني بنجاح!');
            closeLegalModal();
        }

        // Render Finance Dashboard
        function renderFinance() {
            const totalCollected = payments.filter(p => p.status === 'paid').reduce((sum, p) => sum + p.amount, 0);
            const totalOverdue = payments.filter(p => p.status === 'late').reduce((sum, p) => sum + p.amount, 0);
            const totalExpenses = expenses.reduce((sum, e) => sum + e.amount, 0);
            const netProfit = totalCollected - totalExpenses;
            
            document.getElementById('netProfit').textContent = `${netProfit.toLocaleString()} د.ك`;
            document.getElementById('totalCollected').textContent = `${totalCollected.toLocaleString()} د.ك`;
            document.getElementById('totalOverdue').textContent = `${totalOverdue.toLocaleString()} د.ك`;
            document.getElementById('totalExpenses').textContent = `${totalExpenses.toLocaleString()} د.ك`;
            
            // Render Payments
            const paymentsGrid = document.getElementById('paymentsGrid');
            paymentsGrid.innerHTML = '';
            
            payments.forEach(payment => {
                const div = document.createElement('div');
                div.className = 'payment-item';
                
                const statusIcon = payment.status === 'paid' ? '✅' : '🚨';
                const overdueText = payment.status === 'late' ? 
                    `<div class="days-overdue">متأخر ${payment.daysOverdue} يوم</div>` : '';
                
                div.innerHTML = `
                    <div class="payment-status-icon ${payment.status}">${statusIcon}</div>
                    <div class="payment-details">
                        <div class="payment-name">${payment.tenant} - ${payment.property}</div>
                        <div class="payment-amount">${payment.amount} د.ك</div>
                        ${overdueText}
                    </div>
                `;
                
                paymentsGrid.appendChild(div);
            });
            
            // Revenue vs Expenses Chart
            const revenueExpenseData = [{
                x: ['الشهر الحالي'],
                y: [totalCollected],
                name: 'الإيرادات',
                type: 'bar',
                marker: { color: '#10B981' }
            }, {
                x: ['الشهر الحالي'],
                y: [totalExpenses],
                name: 'المصروفات',
                type: 'bar',
                marker: { color: '#EF4444' }
            }];
            
            const revenueExpenseLayout = {
                title: 'الإيرادات مقابل المصروفات',
                font: { family: 'IBM Plex Sans Arabic', color: 'white' },
                paper_bgcolor: 'rgba(0,0,0,0)',
                plot_bgcolor: 'rgba(30,41,59,0.5)',
                barmode: 'group'
            };
            
            Plotly.newPlot('revenueExpenseChart', revenueExpenseData, revenueExpenseLayout, {responsive: true});
            
            // Expense Breakdown Chart
            const expenseBreakdownData = [{
                labels: expenses.map(e => e.name),
                values: expenses.map(e => e.amount),
                type: 'pie',
                hole: 0.4,
                marker: {
                    colors: ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#EC4899']
                }
            }];
            
            const expenseBreakdownLayout = {
                title: 'توزيع المصروفات',
                font: { family: 'IBM Plex Sans Arabic', color: 'white' },
                paper_bgcolor: 'rgba(0,0,0,0)'
            };
            
            Plotly.newPlot('expenseBreakdownChart', expenseBreakdownData, expenseBreakdownLayout, {responsive: true});
        }

        // Render Expenses
        function renderExpenses() {
            const totalExpenses = expenses.reduce((sum, e) => sum + e.amount, 0);
            document.getElementById('totalExpensesDetail').textContent = `${totalExpenses.toLocaleString()} د.ك`;
            
            const expensesGrid = document.getElementById('expensesGrid');
            expensesGrid.innerHTML = '';
            
            expenses.forEach(expense => {
                const percentage = (expense.amount / totalExpenses) * 100;
                
                const div = document.createElement('div');
                div.className = 'expense-card';
                div.innerHTML = `
                    <div class="expense-header">
                        <div class="expense-name">${expense.name}</div>
                        <div class="expense-amount">${expense.amount.toLocaleString()} د.ك</div>
                    </div>
                    <div class="occupancy-bar">
                        <div class="occupancy-fill" style="width: ${percentage}%; background: linear-gradient(90deg, #EF4444 0%, #F87171 100%);"></div>
                    </div>
                    <div class="occupancy-text" style="color: #F87171;">${percentage.toFixed(1)}% من إجمالي المصروفات</div>
                `;
                
                expensesGrid.appendChild(div);
            });
            
            // Expenses Trend Chart
            const months = ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو'];
            const expensesTrend = [12800, 13200, 11900, 13000, 12500, 13000];
            
            const trendData = [{
                x: months,
                y: expensesTrend,
                mode: 'lines+markers',
                name: 'المصروفات',
                line: { color: '#EF4444', width: 3 },
                marker: { size: 10, color: '#D4AF37' }
            }];
            
            const trendLayout = {
                title: 'اتجاه المصروفات (آخر 6 أشهر)',
                font: { family: 'IBM Plex Sans Arabic', color: 'white' },
                paper_bgcolor: 'rgba(0,0,0,0)',
                plot_bgcolor: 'rgba(30,41,59,0.5)',
                xaxis: { title: 'الشهر', gridcolor: 'rgba(100,116,139,0.2)' },
                yaxis: { title: 'المبلغ (د.ك)', gridcolor: 'rgba(100,116,139,0.2)' }
            };
            
            Plotly.newPlot('expensesTrendChart', trendData, trendLayout, {responsive: true});
        }

        // Show View
        function showView(viewName) {
            // Update nav buttons
            document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            // Hide all views
            document.querySelectorAll('.view-content').forEach(view => view.classList.add('hidden'));
            
            // Show selected view
            if (viewName === 'portfolio') {
                document.getElementById('portfolioView').classList.remove('hidden');
                renderProperties();
            } else if (viewName === 'finance') {
                document.getElementById('financeView').classList.remove('hidden');
                renderFinance();
            } else if (viewName === 'expenses') {
                document.getElementById('expensesView').classList.remove('hidden');
                renderExpenses();
            }
        }

        // Enter key login
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('password').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    login();
                }
            });
        });
    </script>
</body>
</html>