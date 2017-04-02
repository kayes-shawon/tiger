from django.db import models

# Create your models here.
class Competing_Brand_Retailer(models.Model):
    m_id = models.IntegerField(max_length=11)
    top_competitor = models.CharField(max_length=200)
    dealer_name = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    avg_sale = models.CharField(max_length=200)
    retailer_com = models.CharField(max_length=200)
    remark = models.TextField(max_length=200)
    class Meta:
        db_table = 'competing_band_ratailer'

class Dealer_Retailer(models.Model):
    id = models.AutoField(primary_key=True)
    d_id = models.ForeignKey(Dev_Dealer, on_delete=models.CASCADE)#Foreign Key Applied
    r_id = models.IntegerField(Dev_Retailer, on_delete = models.CASCADE)#Foreign Key Applied
    class Meta:
        db_table = 'dealer_retailer'

class Dev_Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    class Meta:
        db_table = 'dev_brand'

class Dev_Branding_Activity_Analysis(models.Model):
    id = models.AutoField(primary_key=True)
    submitter_by_employee_id = models.IntegerField(max_length=11)
    territory = models.IntegerField(max_length=11)
    area = models.CharField(max_length=250)
    zone = models.IntegerField(max_length=11)
    month = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=200)
    bill_board = models.CharField(max_length=200)
    shop_sign = models.CharField(max_length=200)
    shop_paint = models.CharField(max_length=200)
    project_sign = models.CharField(max_length=200)
    wall_paint = models.CharField(max_length=200)
    trnasport_paint = models.CharField(max_length=200)
    other_activity = models.CharField(max_length=200)
    name_of_item = models.CharField(max_length=200)
    msons_meet = models.CharField(max_length=200)
    eng_meet = models.CharField(max_length=200)
    dealer_meet = models.CharField(max_length=200)
    sponsor = models.CharField(max_length=200)
    other_event = models.CharField(max_length=200)
    local_cable = models.CharField(max_length=200)
    radio = models.CharField(max_length=200)
    news_paper = models.CharField(max_length=200)
    other_madina = models.CharField(max_length=200)
    created_date = models.IntegerField(max_length=11)
    class Meta:
        db_table = 'dev_branding_activity_analysis'

class Dev_Business_Card_Requisition(models.Model):
    id = models.AutoField(primary_key=True)
    requested_by_employee_id = models.IntegerField(max_length=11)
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    processed = models.SmallIntegerField(max_length=1)
    class Meta:
        db_table = 'dev_business_card_requisition'

class Dev_Competiting_Dealer(models.Model):
    id = models.AutoField(primary_key=True)
    brands = models.CharField(max_length=250)
    landing_brand = models.CharField(max_length=250)
    competing_dealer_name = models.CharField(max_length=250)
    competing_dealer_add = models.CharField(max_length=500)
    competing_dealer_proprietor = models.CharField(max_length=250)
    competing_dealer_mobile = models.CharField(max_length=20)
    credit_recieve_day = models.IntegerField(max_length=20)
    credit_facility_amount = models.CharField(max_length=200)
    dealer_credit_circulation = models.CharField(max_length=200)
    total_retailer = models.IntegerField(max_length=11)
    top_retailer_name = models.CharField(max_length=250)
    tor_retailer_add = models.CharField(max_length=250)
    top_retailer_proprietor = models.CharField(max_length=250)
    top_retailer_mobile = models.CharField(max_length=20)
    commisssion = models.CharField(max_length=20)
    other_package = models.TextField()
    created_date = models.DateField()
    class Meta:
        db_table = 'dev_competiting_dealer'

class Dev_Competitor_Based_Price(models.Model):
    m_id = models.IntegerField(max_length=11)
    brand_id = models.IntegerField(max_length=11)
    market_price = models.IntegerField(max_length=200)
    sales_monthly = models.IntegerField(max_length=200)
    share = models.FloatField()
    unique_activity = models.TextField()
    class Meta:
        db_table = 'dev_competitor_based_price'

class Dev_Competitor_Based_Share(models.Model):
    m_id = models.IntegerField(max_length=11)
    brand_id = models.IntegerField(max_length=11)
    market_share = models.FloatField()
    sales_monthly = models.IntegerField(max_length=11)
    price = models.IntegerField(max_length=11)
    unique_activity = models.TextField()
    class Meta:
        db_table = 'dev_competitor_based_share'

class Dev_Daily_Tour_Plan(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Dev_Employee, on_delete=models.CASCADE)#Foreign Key Applied
    tour_plan = models.CharField(max_length=1000)
    tour_date = models.DateField()
    tracked_location_remarks = models.CharField(max_length=50)
    stats = models.CharField(max_length=20)
    remarks = models.CharField(max_length=200)
    class Meta:
        db_table = 'dev_daily_tour_plan'

class Dev_Dealer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    proprietor = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    mobile = models.CharField(max_length=15)
    submitted_by_employee_id = models.IntegerField(max_length=11)
    class Meta:
        db_table = 'dev_dealer'

class Dev_Dealers_Issue(models.Model):
    id = models.AutoField(primary_key=True)
    dealer_id = models.ForeignKey(Dev_Dealer, on_delete=models.CASCADE)# Foreign Key Applied
    dealer_interview_id = models.IntegerField(max_length=11)
    dealer_issue = models.TextField()
    issue_type = models.TextField()
    sales_rep_statement = models.TextField()
    rsm_asm_recommendation = models.TextField()
    date = models.DateField()
    class Meta:
        db_table = 'dev_dealers_issue'

class Dev_Dealer_Details(models.Model):
    id = models.AutoField(primary_key=True)
    dealer_id = models.IntegerField(max_length=11)
    target_commision = models.IntegerField(max_length=11)
    landing_rate = models.IntegerField(max_length=11)
    other_compensation_packages = models.CharField(max_length=1000)
    security_status = models.TextField()
    created_date = models.DateField()
    class Meta:
        db_table = 'dev_dealer_details'

class Dev_Dealer_Interview(models.Model):
    interview_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(max_length=11)# Foreign Key confusion
    dealer_id = models.ForeignKey(Dev_Dealer, on_delete=models.CASCADE)# Foreign Key Applied
    dealer_name = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    no_district = models.IntegerField(max_length=11)
    no_thana = models.IntegerField(max_length=11)
    no_own_retailer = models.IntegerField(max_length=11)
    no_market_retailer = models.IntegerField(max_length=11)
    interview_date = models.DateField()
    class Meta:
        db_table = 'dev_dealer_interview'

class Dev_Email_Requisition(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_by_employee_id = models.IntegerField(max_length=11)
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    des_email = models.CharField(max_length=200)
    class Meta:
        db_table = 'dev_email_requisition'

class Dev_Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=200)
    zone = models.IntegerField(max_length=11)
    thana = models.CharField(max_length=30)
    mobile = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=255)
    image = models.CharField(max_length=500)
    access_level = models.IntegerField(max_length=11)
    manager_id = models.IntegerField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.SmallIntegerField(max_length=1)
    class Meta:
        db_table = 'dev_employee'

class Dev_Employee_Location(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.IntegerField(max_length=11)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    recorded_timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'dev_employee_location'

class Dev_Gov_Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    submitted_by_emloyee_id = models.IntegerField(max_length=11)
    project_name = models.CharField(max_length=500)
    category = models.CharField(max_length=250)
    project_cost = models.CharField(max_length=500)
    project_status = models.CharField(max_length=250)
    engineer_name = models.CharField(max_length=250)
    designation = models.CharField(max_length=200)
    engineer_number = models.CharField(max_length=15)
    email = models.CharField(max_length=250)
    using_brand_id = models.IntegerField(max_length=11)
    contractor_name = models.CharField(max_length=200)
    contractor_number = models.CharField(max_length=15)
    created_date = models.DateField()
    class Meta:
        db_table = 'dev_gov_project'

class Dev_Id_Card_Requisition(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_by_employee_id = models.IntegerField(max_length=11)
    name = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    unit = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    joining_date = models.DateField()
    date_birth = models.DateField()
    blood_group = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    image = models.CharField(max_length=250)
    class Meta:
        db_table = 'dev_id_card_requisition'

class Dev_Manpower_Requisition(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_by_employee_id = models.IntegerField(max_length=11)
    designation = models.CharField(max_length=250)
    remark = models.CharField(max_length=500)
    class Meta:
        db_table = 'dev_manpower_requisition'

class Dev_Market_Info_Summary(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_by_employee_id = models.IntegerField(max_length=11)
    market_share_tiger = models.FloatField()
    landing_price = models.IntegerField(max_length=11)
    average_sales_monthly = models.IntegerField(max_length=11)
    retailer_segment_1000_count = models.IntegerField(max_length=11)
    retailer_segment_900_count = models.IntegerField(max_length=11)
    retailer_segment_800_count = models.IntegerField(max_length=11)
    retailer_segment_700_count = models.IntegerField(max_length=11)
    retailer_segment_600_count = models.IntegerField(max_length=11)
    retailer_segment_500_count = models.IntegerField(max_length=11)
    retailer_segment_400_count = models.IntegerField(max_length=11)
    retailer_segment_300_count = models.IntegerField(max_length=11)
    retailer_segment_200_count = models.IntegerField(max_length=11)
    retailer_segment_100_count = models.IntegerField(max_length=11)
    created_date = models.DateField()
    class Meta:
        db_table = 'dev_market_info_summary'

class Dev_Market_Pricing_Promo_Packages(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_by_employee_id = models.IntegerField(max_length=11)
    brand_id = models.IntegerField(max_length=11)
    ex_factory = models.CharField(max_length=250)
    transport_cost = models.CharField(max_length=250)
    landing_rate = models.CharField(max_length=200)
    gener = models.CharField(max_length=200)
    target = models.CharField(max_length=200)
    retailer_com = models.CharField(max_length=200)
    p_package = models.CharField(max_length=100)
    incentive_bag = models.CharField(max_length=200)
    promotional_package = models.TextField()
    net_price = models.CharField(max_length=100)
    remark = models.CharField(max_length=200)
    created_date = models.DateField()
    class Meta:
        db_table = 'dev_market_pricing_promo_packages'

class Dev_Market_Share_of_Brand(models.Model):
    id = models.AutoField(primary_key=True)
    market_analysis_id = models.IntegerField(max_length=11)
    thana = models.IntegerField(max_length=11)
    volume = models.IntegerField(max_length=11)
    share = models.FloatField()
    created_date = models.DateField()
    brand_id = models.IntegerField(max_length=11)
    class Meta:
        db_table = 'dev_market_share_of_brand'

class Dev_Market_Share_of_Retailer(models.Model):
    id = models.AutoField(primary_key=True)
    retailer_id = models.IntegerField(max_length=11)
    date = models.DateField()
    total = models.IntegerField(max_length=11)
    volume = models.IntegerField(max_length=11)
    class Meta:
        db_table = 'dev_market_share_of_retailer'

class Dev_Market_Share_of_Retailer_Brand(models.Model):
    id = models.AutoField(primary_key=True)
    market_share_of_retailer_id = models.IntegerField(max_length=11)
    brand_id = models.IntegerField(max_length=11)
    volume = models.IntegerField(max_length=11)
    share = models.IntegerField(max_length=11)
    class Meta:
        db_table = 'dev_market_share_of_retailer_brand'

class Dev_Negative_Aspects(models.Model):
    #negative_aspect_id = models.AutoField(primary_key=True)#Foreign Key
    negative_aspect_id = models.ForeignKey(Market_Analysis,on_delete=models.CASCADE)#Foreign Key Applied
    market_info_summary_id = models.IntegerField(max_length=11)
    aspect = models.TextField()
    class Meta:
        db_table = 'dev_negative_aspects'

class Dev_Opportunity_Info(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_by_employee_id = models.IntegerField(max_length=11)
    created_date = models.DateField()
    report = models.TextField()
    image = models.BinaryField()
    class Meta:
        db_table = 'dev_opportunity_info'

class Dev_Outdoor_Branding_Requisition(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_by_employee_id = models.IntegerField(max_length=11)
    zone = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    thana = models.CharField(max_length=200)
    market_size = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    requirement_name = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=20)
    vendor_name = models.CharField(max_length=200)
    asking_price = models.CharField(max_length=200)
    dealer_number = models.CharField(max_length=200)
    retailer_number = models.CharField(max_length=200)
    class Meta:
        db_table = 'dev_outdoor_branding_requisition'


class Dev_Project_Board_Branding_Requisition(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_by_employee_id = models.IntegerField(max_length=11)
    zone = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    thana = models.CharField(max_length=200)
    project_name = models.CharField(max_length=200)
    project_duration = models.CharField(max_length=200)
    project_address = models.CharField(max_length=250)
    project_monitor_by = models.CharField(max_length=200)
    monthly_consumption = models.CharField(max_length=200)
    class Meta:
        db_table = 'dev_project_board_branding_requisition'

class Dev_Promotional_Info(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_by_employee_id = models.IntegerField(max_length=11)
    detail_promo = models.TextField(max_length=200)
    remark = models.CharField(max_length=250)
    image = models.BinaryField()
    created_date = models.DateField()
    class Meta:
        db_table = 'dev_promotional_info'


class Dev_Report_Problem(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_by_employee_id = models.ForeignKey(Dev_Employee, on_delete=models.CASCADE)#foreign Key
    problem_name = models.TextField(max_length=200)
    description = models.TextField(max_length=250)
    class Meta:
        db_table = 'dev_report_problem'

class Dev_Requisition(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_by_employee_id = models.IntegerField(max_length=11)
    created_date = models.DateField()
    item_name = models.CharField(max_length=250)
    quantity = models.IntegerField(max_length=11)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    image = models.CharField(max_length=250)
    class Meta:
        db_table = 'dev_requisition'

class Dev_Retailer(models.Model):
    r_id = models.AutoField(primary_key=True)
    zone = models.IntegerField(max_length=11)
    district = models.CharField(max_length=200)
    thana = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    d_id = models.IntegerField(max_length=11) #ForeignKey
    proprietor_name = models.CharField(max_length=300)
    address = models.CharField(max_length=500)
    mobile_number = models.CharField(max_length=15)
    bank_name = models.CharField(max_length=100)
    bank_account_name = models.CharField(max_length=200)
    bank_account_no = models.CharField(max_length=200)
    class Meta:
        db_table = 'dev_retailer'

class Dev_Retail_Visit_Info(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.IntegerField(max_length=11)
    retailer_id = models.IntegerField(max_length=11)
    visit_date = models.DateField()
    remarks = models.CharField(max_length=1000)
    gps_location = models.CharField(max_length=40)
    class Meta:
        db_table = 'dev_retail_visit_info'

class Dev_Shop_Branding_Requisition(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_by_employee_id = models.IntegerField(max_length=11)
    zone = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    thana = models.CharField(max_length=200)
    dealer_name = models.CharField(max_length=250)
    retailer_name = models.CharField(max_length=200)
    retailer_contact_no = models.CharField(max_length=200)
    monthly_sales = models.CharField(max_length=200)
    shop_address = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    class Meta:
        db_table = 'dev_shop_branding_requisition'

class Dev_Strategy_Market_Share(models.Model):
    id = models.AutoField(primary_key=True)
    m_id = models.IntegerField(max_length=11)
    strategy = models.TextField()
    class Meta:
        db_table = 'dev_strategy_market_share'

class Do_Requisition(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(max_length=11)
    name = models.CharField(max_length=200)
    tiger = models.CharField(max_length=200)
    extreme = models.CharField(max_length=200)
    opc = models.CharField(max_length=200)
    three_rings = models.CharField(max_length=200)
    buffalo_head = models.CharField(max_length=200)
    free_bag = models.CharField(max_length=200)
    landing_price = models.CharField(max_length=200)
    amount_taka = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=200)
    delivery_point = models.CharField(max_length=200)
    bag_type = models.CharField(max_length=200)
    remark = models.CharField(max_length=250)
    class Meta:
        db_table = 'do_requisition'

class Market_Analysis(models.Model):
    m_id = models.AutoField(primary_key=True)
    info_collected_by = models.CharField(max_length=250)
    recording_date = models.DateField()
    thana = models.CharField(max_length=250)
    info_provider = models.CharField(max_length=200)
    rsm_name = models.CharField(max_length=250)
    rsm_phone = models.CharField(max_length=200)
    landing_price = models.DecimalField(max_digits=10, decimal_places=3)
    projected_sales_monthly = models.IntegerField(max_length=11)
    average_sales = models.DecimalField(max_digits=10, decimal_places=3)