from rc.resources.apps.scrape import parsers
from rc.resources.apps.scrape import loader
from rc.resources.apps.scrape.loader.etl import etl


# register operations
etl.register(parsers.CampusEnergyPlan, loader.GenericLoader, 'operations.EnergyPlanssh')
etl.register(parsers.ElectricVehicleFleet, loader.GenericLoader, 'operations.ElectricFleet')
etl.register(parsers.CarBanParser, loader.CarBanLoader, 'operations.CarBan')
# TODO Biodiesel fleets
etl.register(parsers.BicyclePlans, loader.GenericLoader, 'operations.BicyclePlan')
etl.register(parsers.BuildingEnergyDashboard, loader.BuildingDashboardLoader, 'operations.BuildingDashboard')
etl.register(parsers.AlternativeTransport, loader.GenericLoader, 'operations.TransportationWebsite')
etl.register(parsers.BottledWaterBans, loader.BottleWaterBanLoader, 'operations.BottledWaterBan')
etl.register(parsers.CarSharing, loader.CarShareLoader, 'operations.CarShare')
etl.register(parsers.RecyclingWasteMinimization, loader.RecyclingWasteLoader, 'operations.RecyclingWebsite')

# register education
etl.register(parsers.SustainableLivingGuide, loader.GenericLoader, 'education.LivingGuides', reset=True)
etl.register(parsers.CampusAgriculture, loader.GenericLoader, 'education.CampusAgriculture', reset=True)
etl.register(parsers.SustainabilityResearchInventories, loader.GenericLoader, 'education.ResearchInventories', reset=True)
etl.register(parsers.SustainableCourseInventories, loader.GenericLoader, 'education.SustainabilityCourseInventory', reset=True)
etl.register(parsers.SustainabilitySyllabi, loader.GenericLoader, 'education.SustainabilitySyllabus', reset=True)
etl.register(parsers.FacultyDevelopmentWorkshops, loader.GenericLoader, 'education.FacultyWorkshops', reset=True)
etl.register(parsers.SurveysAwarenessAttitudes, loader.GenericLoader, 'education.SurveyOfAwareness')

# register policies
etl.register(parsers.EnergyPoliciesParser, loader.PolicyLoader,
             'policies.Policy', policy_type='Energy Conservation Policy')
etl.register(parsers.IntegratedPestPolicies, loader.PolicyLoader,
             'policies.Policy', policy_type='Integrated Pest Management Policy')
etl.register(parsers.LicenseeCodeConduct, loader.PolicyLoader,
             'policies.Policy', policy_type='Licensee Code of Conduct')
etl.register(parsers.GreenCleaning, loader.PolicyLoader,
             'policies.Policy', policy_type='Green Cleaning Procurement Policy')
etl.register(parsers.RecyclingPolicy, loader.PolicyLoader,
             'policies.Policy', policy_type='Recycling / Waste Minimization Policy')
etl.register(parsers.GeneralProcurementPolicies, loader.PolicyLoader,
             'policies.Policy', policy_type='General / Comprehensive Procurement Policy')
