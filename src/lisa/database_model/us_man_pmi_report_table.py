from types import MappingProxyType

from sqlalchemy import REAL, Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class US_Man_Pmi_Report(Base):
    __tablename__ = "US_Man_Pmi_Report"
    year = Column(Integer, primary_key=True)
    month = Column(Integer, primary_key=True)
    headline = Column(Text)
    highlights = Column(Text)
    overview = Column(Text)
    comments = Column(Text)
    commodities_up = Column(Text)
    commodities_down = Column(Text)
    commodities_short = Column(Text)
    index_summary = Column(Text)
    new_orders = Column(Text)
    production = Column(Text)
    employment = Column(Text)
    supplier_deliveries = Column(Text)
    inventories = Column(Text)
    customer_inventories = Column(Text)
    prices = Column(Text)
    backlog_orders = Column(Text)
    export_orders = Column(Text)
    imports = Column(Text)
    buying_policy = Column(Text)
    pmi_index_value = Column(REAL)
    pmi_direction = Column(Text)
    pmi_change_rate = Column(Text)
    pmi_trend_months = Column(Integer)
    new_orders_index_value = Column(REAL)
    new_orders_direction = Column(Text)
    new_orders_change_rate = Column(Text)
    new_orders_trend_months = Column(Integer)
    production_index_value = Column(REAL)
    production_direction = Column(Text)
    production_change_rate = Column(Text)
    production_trend_months = Column(Integer)
    employment_index_value = Column(REAL)
    employment_direction = Column(Text)
    employment_change_rate = Column(Text)
    employment_trend_months = Column(Integer)
    supplier_deliveries_index_value = Column(REAL)
    supplier_deliveries_direction = Column(Text)
    supplier_deliveries_change_rate = Column(Text)
    supplier_deliveries_trend_months = Column(Integer)
    inventories_index_value = Column(REAL)
    inventories_direction = Column(Text)
    inventories_change_rate = Column(Text)
    inventories_trend_months = Column(Integer)
    customer_inventories_index_value = Column(REAL)
    customer_inventories_direction = Column(Text)
    customer_inventories_change_rate = Column(Text)
    customer_inventories_trend_months = Column(Integer)
    prices_index_value = Column(REAL)
    prices_direction = Column(Text)
    prices_change_rate = Column(Text)
    prices_trend_months = Column(Integer)
    backlog_orders_index_value = Column(REAL)
    backlog_orders_direction = Column(Text)
    backlog_orders_change_rate = Column(Text)
    backlog_orders_trend_months = Column(Integer)
    export_orders_index_value = Column(REAL)
    export_orders_direction = Column(Text)
    export_orders_change_rate = Column(Text)
    export_orders_trend_months = Column(Integer)
    imports_index_value = Column(REAL)
    imports_direction = Column(Text)
    imports_change_rate = Column(Text)
    imports_trend_months = Column(Integer)
    overall_economy_direction = Column(Text)
    overall_economy_change_rate = Column(Text)
    overall_economy_trend_months = Column(Integer)
    manufacturing_sector_direction = Column(Text)
    manufacturing_sector_change_rate = Column(Text)
    manufacturing_sector_trend_months = Column(Integer)
    new_orders_higher_pct = Column(REAL)
    new_orders_same_pct = Column(REAL)
    new_orders_lower_pct = Column(REAL)
    production_higher_pct = Column(REAL)
    production_same_pct = Column(REAL)
    production_lower_pct = Column(REAL)
    employment_higher_pct = Column(REAL)
    employment_same_pct = Column(REAL)
    employment_lower_pct = Column(REAL)
    supplier_deliveries_slower_pct = Column(REAL)
    supplier_deliveries_same_pct = Column(REAL)
    supplier_deliveries_faster_pct = Column(REAL)
    inventories_higher_pct = Column(REAL)
    inventories_same_pct = Column(REAL)
    inventories_lower_pct = Column(REAL)
    customer_inventories_reporting_pct = Column(REAL)
    customer_inventories_too_high_pct = Column(REAL)
    customer_inventories_about_right_pct = Column(REAL)
    customer_inventories_too_low_pct = Column(REAL)
    prices_higher_pct = Column(REAL)
    prices_same_pct = Column(REAL)
    prices_lower_pct = Column(REAL)
    backlog_orders_reporting_pct = Column(REAL)
    backlog_orders_higher_pct = Column(REAL)
    backlog_orders_same_pct = Column(REAL)
    backlog_orders_lower_pct = Column(REAL)
    export_orders_reporting_pct = Column(REAL)
    export_orders_higher_pct = Column(REAL)
    export_orders_same_pct = Column(REAL)
    export_orders_lower_pct = Column(REAL)
    imports_reporting_pct = Column(REAL)
    imports_higher_pct = Column(REAL)
    imports_same_pct = Column(REAL)
    imports_lower_pct = Column(REAL)
    capex_lead_time_avg = Column(Integer)
    capex_lead_time_hand_to_mouth_pct = Column(REAL)
    capex_lead_time_thirty_days_pct = Column(REAL)
    capex_lead_time_sixty_days_pct = Column(REAL)
    capex_lead_time_ninety_days_pct = Column(REAL)
    capex_lead_time_six_months_pct = Column(REAL)
    capex_lead_time_year_plus_pct = Column(REAL)
    production_lead_time_avg = Column(Integer)
    production_lead_time_hand_to_mouth_pct = Column(REAL)
    production_lead_time_thirty_days_pct = Column(REAL)
    production_lead_time_sixty_days_pct = Column(REAL)
    production_lead_time_ninety_days_pct = Column(REAL)
    production_lead_time_six_months_pct = Column(REAL)
    production_lead_time_year_plus_pct = Column(REAL)
    mro_lead_time_avg = Column(Integer)
    mro_lead_time_hand_to_mouth_pct = Column(REAL)
    mro_lead_time_thirty_days_pct = Column(REAL)
    mro_lead_time_sixty_days_pct = Column(REAL)
    mro_lead_time_ninety_days_pct = Column(REAL)
    mro_lead_time_six_months_pct = Column(REAL)
    mro_lead_time_year_plus_pct = Column(REAL)
    apparel_comments = Column(Text)
    chemical_comments = Column(Text)
    computer_electronics_comments = Column(Text)
    electrical_equipment_comments = Column(Text)
    fabricated_metal_comments = Column(Text)
    food_beverage_tobacco_comments = Column(Text)
    furniture_comments = Column(Text)
    machinery_comments = Column(Text)
    miscellaneous_comments = Column(Text)
    non_metallic_mineral_comments = Column(Text)
    paper_comments = Column(Text)
    petroleum_coal_comments = Column(Text)
    plastic_rubber_comments = Column(Text)
    metals_comments = Column(Text)
    printing_comments = Column(Text)
    textiles_comments = Column(Text)
    transportation_comments = Column(Text)
    wood_comments = Column(Text)

    @classmethod
    def name(cls):
        return cls.__tablename__

    @classmethod
    def columns(cls):
        return [c.name for c in cls.__table__.columns]

    @staticmethod
    def column_map():
        return MappingProxyType(
            {
                "year": "year",
                "month": "month",
                "headline": "headline",
                "highlights": "highlights",
                "overview": "overview",
                "comments": "comments",
                "commodities_up": "commodities_up",
                "commodities_down": "commodities_down",
                "commodities_short": "commodities_short",
                "index_summary": "index_summary",
                "new_orders": "new_orders",
                "production": "production",
                "employment": "employment",
                "supplier_deliveries": "supplier_deliveries",
                "inventories": "inventories",
                "customer_inventories": "customer_inventories",
                "prices": "prices",
                "backlog_orders": "backlog_orders",
                "export_orders": "export_orders",
                "imports": "imports",
                "buying_policy": "buying_policy",
                "pmi_index_value": "pmi_index_value",
                "pmi_direction": "pmi_direction",
                "pmi_change_rate": "pmi_change_rate",
                "pmi_trend_months": "pmi_trend_months",
                "new_orders_index_value": "new_orders_index_value",
                "new_orders_direction": "new_orders_direction",
                "new_orders_change_rate": "new_orders_change_rate",
                "new_orders_trend_months": "new_orders_trend_months",
                "production_index_value": "production_index_value",
                "production_direction": "production_direction",
                "production_change_rate": "production_change_rate",
                "production_trend_months": "production_trend_months",
                "employment_index_value": "employment_index_value",
                "employment_direction": "employment_direction",
                "employment_change_rate": "employment_change_rate",
                "employment_trend_months": "employment_trend_months",
                "supplier_deliveries_index_value": "supplier_deliveries_index_value",
                "supplier_deliveries_direction": "supplier_deliveries_direction",
                "supplier_deliveries_change_rate": "supplier_deliveries_change_rate",
                "supplier_deliveries_trend_months": "supplier_deliveries_trend_months",
                "inventories_index_value": "inventories_index_value",
                "inventories_direction": "inventories_direction",
                "inventories_change_rate": "inventories_change_rate",
                "inventories_trend_months": "inventories_trend_months",
                "customer_inventories_index_value": "customer_inventories_index_value",
                "customer_inventories_direction": "customer_inventories_direction",
                "customer_inventories_change_rate": "customer_inventories_change_rate",
                "customer_inventories_trend_months": "customer_inventories_trend_months",
                "prices_index_value": "prices_index_value",
                "prices_direction": "prices_direction",
                "prices_change_rate": "prices_change_rate",
                "prices_trend_months": "prices_trend_months",
                "backlog_orders_index_value": "backlog_orders_index_value",
                "backlog_orders_direction": "backlog_orders_direction",
                "backlog_orders_change_rate": "backlog_orders_change_rate",
                "backlog_orders_trend_months": "backlog_orders_trend_months",
                "export_orders_index_value": "export_orders_index_value",
                "export_orders_direction": "export_orders_direction",
                "export_orders_change_rate": "export_orders_change_rate",
                "export_orders_trend_months": "export_orders_trend_months",
                "imports_index_value": "imports_index_value",
                "imports_direction": "imports_direction",
                "imports_change_rate": "imports_change_rate",
                "imports_trend_months": "imports_trend_months",
                "overall_economy_direction": "overall_economy_direction",
                "overall_economy_change_rate": "overall_economy_change_rate",
                "overall_economy_trend_months": "overall_economy_trend_months",
                "manufacturing_sector_direction": "manufacturing_sector_direction",
                "manufacturing_sector_change_rate": "manufacturing_sector_change_rate",
                "manufacturing_sector_trend_months": "manufacturing_sector_trend_months",
                "new_orders_higher_pct": "new_orders_higher_pct",
                "new_orders_same_pct": "new_orders_same_pct",
                "new_orders_lower_pct": "new_orders_lower_pct",
                "production_higher_pct": "production_higher_pct",
                "production_same_pct": "production_same_pct",
                "production_lower_pct": "production_lower_pct",
                "employment_higher_pct": "employment_higher_pct",
                "employment_same_pct": "employment_same_pct",
                "employment_lower_pct": "employment_lower_pct",
                "supplier_deliveries_slower_pct": "supplier_deliveries_slower_pct",
                "supplier_deliveries_same_pct": "supplier_deliveries_same_pct",
                "supplier_deliveries_faster_pct": "supplier_deliveries_faster_pct",
                "inventories_higher_pct": "inventories_higher_pct",
                "inventories_same_pct": "inventories_same_pct",
                "inventories_lower_pct": "inventories_lower_pct",
                "customer_inventories_reporting_pct": "customer_inventories_reporting_pct",
                "customer_inventories_too_high_pct": "customer_inventories_too_high_pct",
                "customer_inventories_about_right_pct": "customer_inventories_about_right_pct",
                "customer_inventories_too_low_pct": "customer_inventories_too_low_pct",
                "prices_higher_pct": "prices_higher_pct",
                "prices_same_pct": "prices_same_pct",
                "prices_lower_pct": "prices_lower_pct",
                "backlog_orders_reporting_pct": "backlog_orders_reporting_pct",
                "backlog_orders_higher_pct": "backlog_orders_higher_pct",
                "backlog_orders_same_pct": "backlog_orders_same_pct",
                "backlog_orders_lower_pct": "backlog_orders_lower_pct",
                "export_orders_reporting_pct": "export_orders_reporting_pct",
                "export_orders_higher_pct": "export_orders_higher_pct",
                "export_orders_same_pct": "export_orders_same_pct",
                "export_orders_lower_pct": "export_orders_lower_pct",
                "imports_reporting_pct": "imports_reporting_pct",
                "imports_higher_pct": "imports_higher_pct",
                "imports_same_pct": "imports_same_pct",
                "imports_lower_pct": "imports_lower_pct",
                "capex_lead_time_avg": "capex_lead_time_avg",
                "capex_lead_time_hand_to_mouth_pct": "capex_lead_time_hand_to_mouth_pct",
                "capex_lead_time_thirty_days_pct": "capex_lead_time_thirty_days_pct",
                "capex_lead_time_sixty_days_pct": "capex_lead_time_sixty_days_pct",
                "capex_lead_time_ninety_days_pct": "capex_lead_time_ninety_days_pct",
                "capex_lead_time_six_months_pct": "capex_lead_time_six_months_pct",
                "capex_lead_time_year_plus_pct": "capex_lead_time_year_plus_pct",
                "production_lead_time_avg": "production_lead_time_avg",
                "production_lead_time_hand_to_mouth_pct": "production_lead_time_hand_to_mouth_pct",
                "production_lead_time_thirty_days_pct": "production_lead_time_thirty_days_pct",
                "production_lead_time_sixty_days_pct": "production_lead_time_sixty_days_pct",
                "production_lead_time_ninety_days_pct": "production_lead_time_ninety_days_pct",
                "production_lead_time_six_months_pct": "production_lead_time_six_months_pct",
                "production_lead_time_year_plus_pct": "production_lead_time_year_plus_pct",
                "mro_lead_time_avg": "mro_lead_time_avg",
                "mro_lead_time_hand_to_mouth_pct": "mro_lead_time_hand_to_mouth_pct",
                "mro_lead_time_thirty_days_pct": "mro_lead_time_thirty_days_pct",
                "mro_lead_time_sixty_days_pct": "mro_lead_time_sixty_days_pct",
                "mro_lead_time_ninety_days_pct": "mro_lead_time_ninety_days_pct",
                "mro_lead_time_six_months_pct": "mro_lead_time_six_months_pct",
                "mro_lead_time_year_plus_pct": "mro_lead_time_year_plus_pct",
                "Apparel, Leather & Allied Products": "apparel_comments",
                "Chemical Products": "chemical_comments",
                "Computer & Electronic Products": "computer_electronics_comments",
                "Electrical Equipment, Appliances & Components": "electrical_equipment_comments",
                "Fabricated Metal Products": "fabricated_metal_comments",
                "Food, Beverage & Tobacco Products": "food_beverage_tobacco_comments",
                "Furniture & Related Products": "furniture_comments",
                "Machinery": "machinery_comments",
                "Miscellaneous Manufacturing": "miscellaneous_comments",
                "Nonmetallic Mineral Products": "non_metallic_mineral_comments",
                "Paper Products": "paper_comments",
                "Petroleum & Coal Products": "petroleum_coal_comments",
                "Plastics & Rubber Products": "plastic_rubber_comments",
                "Primary Metals": "metals_comments",
                "Printing & Related Support Activities": "printing_comments",
                "Textile Mills": "textiles_comments",
                "Transportation Equipment": "transportation_comments",
                "Wood Products": "wood_comments",
            }
        )
