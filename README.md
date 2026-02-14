# Glory to God Vehicles

**Fleet Financial, Compliance & Hire Purchase Management System**

---

## 📖 Overview

Glory to God Vehicles is a professional Django-based fleet management and accounting platform for motorbikes and other locomotives operating under hire purchase and rider agreements. Designed for scalable, multi-vehicle operations, it combines:

- Fleet Management
- Hire Purchase Tracking
- Rider Contract Management
- Maintenance & Component Tracking
- Compliance Documentation
- Double-Entry Accounting
- Revenue & Profit Analytics
- PDF Report Generation
- Financial Intelligence Dashboard

## 🎯 Objectives

Fleet owners can:
- Track multiple vehicles
- Monitor hire purchase liabilities
- Measure daily, monthly, and annual profitability
- Manage rider agreements and remittances
- Store compliance and legal documentation
- Track maintenance costs and receipts
- Monitor downtime and service performance
- Generate professional PDF financial reports
- Make data-driven fleet expansion decisions

---

## 🏗 System Architecture

**Backend:**
- Django
- MySQL
- Django ORM
- ReportLab (PDF generation)
- Pillow (image handling)

**Storage:**
- Vehicle, rider, receipt images
- Contract PDFs
- Compliance documents

---
## 📦 Core Modules
### 💸 Payments Module

The Payments Module is designed for robust tracking of all vehicle-related payments, especially for hire purchase and M-Pesa-based transactions (common in Kenya). M-Pesa transaction codes are entered manually—no API integration is required.

#### Core Fields

| Field          | Type      | Description                                 |
|--------------- |---------- |---------------------------------------------|
| id             | UUID      | Unique payment ID                           |
| vehicle_id     | UUID      | Linked vehicle                              |
| contract_id    | UUID      | Linked hire purchase contract               |
| paid_from      | String    | Who sent the money (Driver/Rider/Owner)     |
| paid_to        | String    | Who received the money                      |
| amount         | Decimal   | Amount paid                                 |
| payment_type   | Enum      | installment / penalty / deposit / repair / insurance |
| mpesa_code     | String    | M-Pesa transaction code (e.g. QGH7S8D9F1)   |
| phone_number   | String    | Sender’s M-Pesa phone                       |
| date_paid      | DateTime  | When payment was made                       |
| recorded_at    | DateTime  | When entered into system                    |
| notes          | Text      | Optional remarks                            |
| receipt_image  | File URL  | Uploaded screenshot or receipt              |

#### Example JSON Structure

```json
{
	"id": "pay_001",
	"vehicle_id": "veh_123",
	"contract_id": "con_456",
	"paid_from": "driver_002",
	"paid_to": "owner_001",
	"amount": 15000,
	"payment_type": "installment",
	"mpesa_code": "QGH7S8D9F1",
	"phone_number": "254712345678",
	"date_paid": "2026-02-14T09:30:00",
	"recorded_at": "2026-02-14T10:00:00",
	"notes": "February installment",
	"receipt_image": "uploads/payments/pay_001.jpg"
}
```

#### Supported Payment Types

```python
enum PaymentType {
	INSTALLMENT,
	DEPOSIT,
	PENALTY,
	INSURANCE,
	SERVICE,
	REPAIR,
	OTHER
}
```

#### UI Design (Vehicle Profile → Payments Tab)

Display a table with:

| Date        | Paid From   | Paid To     | Amount  | Type        | M-Pesa Code   | Receipt |
|-------------|-------------|-------------|---------|-------------|--------------|---------|
| 14 Feb 2026 | John Rider  | Elvis Owner | 15,000  | Installment | QGH7S8D9F1    | View    |

#### Advanced Features (Recommended)

- **Manual M-Pesa Entry:** M-Pesa codes are keyed in by the user. No Safaricom Daraja API integration is required.
- **Installment Progress Tracker:** Show actual price, hire purchase price, paid so far, balance, and a progress bar in the vehicle profile.
- **Overdue Detection Logic:**
	```python
	if today > due_date and installment_not_paid:
			mark status = OVERDUE
			apply penalty
			send SMS reminder
	```
	Integrate SMS via Africa's Talking.
- **Receipt Image Storage:** Store in `/uploads/vehicles/{vehicle_id}/payments/` using Cloudinary, AWS S3, or Firebase Storage.

#### Database Table (SQL Example)

```sql
CREATE TABLE payments (
		id UUID PRIMARY KEY,
		vehicle_id UUID REFERENCES vehicles(id),
		contract_id UUID REFERENCES contracts(id),
		paid_from VARCHAR(255),
		paid_to VARCHAR(255),
		amount DECIMAL(12,2),
		payment_type VARCHAR(50),
		mpesa_code VARCHAR(50),
		phone_number VARCHAR(20),
		date_paid TIMESTAMP,
		recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		notes TEXT,
		receipt_image TEXT
);
```

#### 🔥 Bonus: Smart Filtering

Allow filtering by:
- Date range
- Payment type
- Paid from
- Paid to
- M-Pesa code
- Verified / Unverified

---

### 1️⃣ User & Role Management
- Admin, Accountant, Manager, Viewer/Auditor
- Role-based access control

### 2️⃣ Vehicle Management
- Registration number, make & model, engine & chassis number
- Actual purchase price, hire purchase price, deposit paid
- Monthly installment, installment period, outstanding balance (auto-calculated)
- Status (Active, Inactive, Under Repair, Retired)
- Vehicle image
- Financial calculations:

	- Interest = Hire Purchase Price – Actual Price
	- Outstanding = Hire Purchase Price – Total Paid
	- Recovery % = Net Profit / Actual Price × 100

### 3️⃣ Rider Management
- Personal details, national ID, phone number, passport photo
- Assigned vehicle
- Rider documents (license, ID copy, etc.)
- Active/Inactive status

### 4️⃣ Rider–Owner Contract Module
- Contract start & end date
- Revenue model: Fixed daily remittance, percentage share, hybrid
- Security deposit, terms & conditions
- Signed contract upload
- Contract status
- PDF contract generation

### 5️⃣ Hire Purchase & Liabilities
- Loan amount, installment schedule, interest, outstanding balance
- Liability ratio: Outstanding / Hire Purchase Price

### 6️⃣ Daily Revenue Tracking
- Daily collections, rider remittances
- Expected vs actual revenue
- Revenue analytics: daily, monthly, annual, per active day, fleet summary

### 7️⃣ Expense & Maintenance Tracking
- Fuel, repairs, spare parts, insurance, licenses, penalties, other expenses
- Date, amount, category, description, receipt image
- Automatic accounting entry

### 8️⃣ Component & Service Records
- Component purchased, supplier, warranty expiry, service type, mechanic details
- Receipt image, service date, next service due date
- Maintenance cost analysis, failure frequency, mechanic performance

### 9️⃣ Odometer & Performance Tracking
- Mileage logs, service intervals, cost/revenue per kilometer

### 🔟 Service & Downtime Logs
- In-service days, off days, downtime reasons (mechanical, maintenance, accident, regulatory, personal leave)
- Fleet Utilization Rate = Active Days / Total Days

### 1️⃣1️⃣ Compliance & Documentation
- Logbook, insurance, road license, inspection, SACCO, hire purchase, lease agreements
- Document number, issue/expiry date, uploaded file
- Expiry alerts

### 1️⃣2️⃣ Accounting Module (Double Entry)
- Chart of Accounts: Assets, Liabilities, Equity, Income, Expenses
- Automatic journal entries: revenue, expenses, liability payments, maintenance, fuel
- Validation: Total Debits = Total Credits

### 1️⃣3️⃣ Financial Intelligence Dashboard
- Total fleet value, outstanding liabilities, monthly revenue, net profit
- Most profitable/highest maintenance vehicle
- Compliance/contract expiry alerts

### 📄 PDF Reports
- Vehicle Financial Report, Monthly Profit Report, Annual Summary
- Rider Statement, Hire Purchase Statement, Maintenance Summary
- Compliance Report, Contract Agreement, Expense Summary, Fleet Performance Report

---

Annual revenue

Revenue per active day

Fleet revenue summary

7️⃣ Expense & Maintenance Tracking

Tracks:

Fuel purchases

Repairs

Spare parts

Insurance

Licenses

---

## 📊 Key Financial Metrics

- **Net Profit:** Total Revenue – Total Expenses – Liability Payments
- **Break-even %:** Total Net Profit / Actual Price × 100
- **Asset ROI:** Annual Net Profit / Actual Price × 100
- **Revenue per Active Day:** Total Revenue / In-Service Days

---

## 🔐 Data Integrity & Security
- Atomic database transactions
- Immutable financial records after posting
- Audit logging
- Role-based permissions
- Secure media storage
- Soft deletion for financial entries

---

## 📁 Project Structure

```
glory_to_god_vehicles/
├── users/
├── fleet/
├── riders/
├── contracts/
├── finance/
├── accounting/
├── maintenance/
├── compliance/
├── reports/
├── dashboard/
├── media/
├── static/
└── templates/
```

---

## ⚙ Installation Guide

1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Configure MySQL database
5. Run migrations
6. Create superuser
7. Run development server

---

## 🚀 Getting Started

1. Clone the repo:
	```bash
	git clone <repo-url>
	```
2. Create and activate a virtual environment:
	```bash
	python -m venv venv
	venv\Scripts\activate
	```
3. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
4. Configure your MySQL database in `settings.py`.
5. Run migrations:
	```bash
	python manage.py migrate
	```
6. Create a superuser:
	```bash
	python manage.py createsuperuser
	```
7. Start the development server:
	```bash
	python manage.py runserver
	```

---

## 🔮 Future Enhancements
- SMS payment reminders
- Digital signature integration
- Multi-branch support
- Multi-currency support
- Mobile app integration
- Cash flow forecasting engine
- Tax computation module
- Fleet expansion recommendation engine

---

## 🏆 System Capabilities Summary

For every vehicle, the system provides:
- Full financial profile
- Hire purchase visibility
- Revenue tracking
- Expense tracking
- Maintenance intelligence
- Compliance monitoring
- Legal contract management
- Profitability analytics
- Risk assessment
- Asset recovery tracking

---

## 📌 Project Vision

To build a professional, scalable, and financially intelligent fleet management system that enables transparent operations, legal compliance, and informed investment decisions.