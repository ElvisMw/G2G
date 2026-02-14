Glory to God Vehicles

Fleet Financial, Compliance & Hire Purchase Management System

📖 Overview

Glory to God Vehicles is a professional Django-based fleet management and accounting system designed to manage motorbikes and other locomotives operating under hire purchase and rider agreements.

This platform combines:

Fleet Management

Hire Purchase Tracking

Rider Contract Management

Maintenance & Component Tracking

Compliance Documentation

Double-Entry Accounting

Revenue & Profit Analytics

PDF Report Generation

Financial Intelligence Dashboard

It is designed for scalable multi-vehicle fleet operations.

🎯 Objectives

This system enables fleet owners to:

Track multiple vehicles

Monitor hire purchase liabilities

Measure daily, monthly, and annual profitability

Manage rider agreements and remittances

Store compliance and legal documentation

Track maintenance costs and receipts

Monitor downtime and service performance

Generate professional PDF financial reports

Make data-driven fleet expansion decisions

🏗 System Architecture
Backend

Django

MySQL

Django ORM

ReportLab (PDF generation)

Pillow (image handling)

Storage

Media storage for:

Vehicle images

Rider images

Receipt images

Contract PDFs

Compliance documents

📦 Core Modules
1️⃣ User & Role Management

Admin

Accountant

Manager

Viewer/Auditor

Role-based access control.

2️⃣ Vehicle Management

Each vehicle profile contains:

Registration number

Make & model

Engine & chassis number

Actual purchase price (cash price)

Hire purchase price

Deposit paid

Monthly installment

Installment period

Outstanding balance (auto-calculated)

Status (Active, Inactive, Under Repair, Retired)

Vehicle image

Financial calculations:

Interest = Hire Purchase Price – Actual Price
Outstanding = Hire Purchase Price – Total Paid
Recovery % = Net Profit / Actual Price × 100

3️⃣ Rider Management

Each rider profile includes:

Personal details

National ID

Phone number

Passport photo

Assigned vehicle

Rider documents (license, ID copy, etc.)

Active/Inactive status

4️⃣ Rider–Owner Contract Module

Manages agreements between fleet owner and rider.

Contract features:

Contract start & end date

Revenue model:

Fixed daily remittance

Percentage share

Hybrid model

Security deposit

Terms & conditions

Signed contract upload

Contract status

Supports PDF contract generation.

5️⃣ Hire Purchase & Liabilities

Tracks:

Loan amount

Installment schedule

Interest

Outstanding balance

Liability ratio

Liability Ratio = Outstanding / Hire Purchase Price

6️⃣ Daily Revenue Tracking

Tracks:

Daily collections

Rider remittances

Expected vs actual revenue

Revenue analytics:

Daily revenue

Monthly revenue

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

Penalties

Other operational expenses

Each expense includes:

Date

Amount

Category

Description

Receipt image

Automatic accounting entry created on save.

8️⃣ Component & Service Records

Tracks:

Component purchased

Supplier

Warranty expiry

Service type

Mechanic details

Receipt image

Service date

Next service due date

Enables:

Maintenance cost analysis

Failure frequency tracking

Mechanic performance analysis

9️⃣ Odometer & Performance Tracking

Tracks:

Mileage logs

Service intervals

Cost per kilometer

Revenue per kilometer

🔟 Service & Downtime Logs

Tracks:

In-service days

Off days

Downtime reasons:

Mechanical breakdown

Scheduled maintenance

Accident damage

Regulatory issue

Rider personal leave

Calculations:

Fleet Utilization Rate = Active Days / Total Days

1️⃣1️⃣ Compliance & Documentation

Vehicle documentation includes:

Logbook

Insurance certificate

Road license

Inspection certificate

SACCO membership

Hire purchase agreement

Lease agreement

Each document includes:

Document number

Issue date

Expiry date

Uploaded file

Expiry alerts generated automatically.

1️⃣2️⃣ Accounting Module (Double Entry)

Chart of Accounts:

Assets

Liabilities

Equity

Income

Expenses

Automatic journal entries for:

Revenue

Expenses

Liability payments

Maintenance

Fuel purchases

Validation rule:

Total Debits = Total Credits

1️⃣3️⃣ Financial Intelligence Dashboard

Displays:

Total fleet value

Outstanding liabilities

Monthly revenue

Net profit

Most profitable vehicle

Highest maintenance vehicle

Compliance alerts

Contract expiry alerts

📄 PDF Reports

Generated using ReportLab.

Available reports:

Vehicle Financial Report

Monthly Profit Report

Annual Summary

Rider Statement

Hire Purchase Statement

Maintenance Summary

Compliance Report

Contract Agreement

Expense Summary

Fleet Performance Report

📊 Key Financial Metrics

Net Profit:

Net Profit = Total Revenue – Total Expenses – Liability Payments


Break-even Percentage:

Break-even % = Total Net Profit / Actual Price × 100


Asset ROI:

ROI = Annual Net Profit / Actual Price × 100


Revenue per Active Day:

Total Revenue / In-Service Days

🔐 Data Integrity & Security

Atomic database transactions

Immutable financial records after posting

Audit logging

Role-based permissions

Secure media storage

Soft deletion for financial entries

📁 Project Structure
glory_to_god_vehicles/
│
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

⚙ Installation Guide

Clone repository

Create virtual environment

Install dependencies

Configure MySQL database

Run migrations

Create superuser

Run development server

🔮 Future Enhancements

SMS payment reminders

Digital signature integration

Multi-branch support

Multi-currency support

Mobile app integration

Cash flow forecasting engine

Tax computation module

Fleet expansion recommendation engine

🏆 System Capabilities Summary

For every vehicle, the system provides:

Full financial profile

Hire purchase visibility

Revenue tracking

Expense tracking

Maintenance intelligence

Compliance monitoring

Legal contract management

Profitability analytics

Risk assessment

Asset recovery tracking

📌 Project Vision

To build a professional, scalable, and financially intelligent fleet management system that enables transparent operations, legal compliance, and informed investment decisions.