from rc.resources.apps.scrape import parsers
from rc.resources.apps.scrape import loader
from rc.resources.apps.scrape.loader.etl import etl


# register operations
etl.register(parsers.WebsiteCampusGreenBuilding, loader.GenericLoader, 'operations.GreenBuildingWebsite')
etl.register(parsers.UniversalAccess, loader.TransitPassLoader, 'operations.TransitPass')
etl.register(parsers.SustainabilityPurchasing, loader.SustainabilityPurchasingLoader, 'operations.PurchasingLink')
etl.register(parsers.SustainableLandscaping, loader.GenericLoader, 'operations.SustainableLandscape')
etl.register(parsers.SustainableDiningInitiatives, loader.SustainableDiningInitiativesLoader, 'operations.DiningInitiative')
etl.register(parsers.FuelCells, loader.GenericLoader, 'operations.FuelCell')
etl.register(parsers.RenewableEnergyResearchCenters, loader.GenericLoader, 'operations.RenewableResearchCenter')
# TODO Publications on Climate Action
# BEGIN Green Buildings
etl.register(parsers.GreenAthleticBuilding, loader.GreenBuildingLoader, 'operations.CampusGreenBuilding')
etl.register(parsers.GreenLibrary, loader.GreenBuildingLoader, 'operations.CampusGreenBuilding')
etl.register(parsers.GreenStudentCenter, loader.GreenBuildingLoader, 'operations.CampusGreenBuilding')
etl.register(parsers.GreenResidence, loader.GreenBuildingLoader, 'operations.CampusGreenBuilding')
etl.register(parsers.GreenScience, loader.GreenBuildingLoader, 'operations.CampusGreenBuilding')
# END
etl.register(parsers.WindTurbine, loader.WindTurbineLoader, 'operations.WindTurbine')
etl.register(parsers.WaterConservation, loader.GenericLoader, 'operations.WaterConservationEffort')
etl.register(parsers.EnergyPoliciesParser, loader.GenericLoader, 'operations.EnergyPolicy')
etl.register(parsers.HybridVehicles, loader.HybridFleetLoader, 'operations.HybridFleet')
# TODO global warming commitments 
etl.register(parsers.CampusEnergyWebsite, loader.GenericLoader, 'operations.EnergyWebsite')
etl.register(parsers.CampusEnergyPlan, loader.GenericLoader, 'operations.EnergyPlan')
etl.register(parsers.ElectricVehicleFleet, loader.GenericLoader, 'operations.ElectricFleet')
etl.register(parsers.CarBan, loader.CarBanLoader, 'operations.CarBan')
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
etl.register(parsers.policies.EnergyConservationPolicies, loader.PolicyLoader,
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
             
# register PAE
etl.register(parsers.AlumniSustainabilityFunds, loader.GenericLoader, 'pae.AlumniFund')
etl.register(parsers.CampusMasterPlan, loader.GenericLoader, 'pae.MasterPlan')
etl.register(parsers.AssessmentTools, loader.AssessmentToolsLoader, 'pae.AssessmentTool')
etl.register(parsers.SustainabilityBlog, loader.GenericLoader, 'pae.SustainabilityBlog')
etl.register(parsers.SustainabilityPlan, loader.GenericLoader, 'pae.SustainabilityPlan')
etl.register(parsers.RevolvingFund, loader.GenericLoader, 'pae.RevolvingLoanFund')
