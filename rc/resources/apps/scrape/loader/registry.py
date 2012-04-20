from rc.resources.apps.scrape import parsers
from rc.resources.apps.scrape import loader
from rc.resources.apps.scrape.loader.etl import etl


# register operations
etl.register(parsers.CommuterSurvey, loader.CommuterSurveyLoader, 'operations.CommuterSurvey')
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
# END Green Buildings
etl.register(parsers.WindTurbine, loader.WindTurbineLoader, 'operations.WindTurbine')
etl.register(parsers.WaterConservation, loader.GenericLoader, 'operations.WaterConservationEffort')
etl.register(parsers.HybridVehicles, loader.HybridFleetLoader, 'operations.HybridFleet')
etl.register(parsers.GlobalWarmingCommitment, loader.GenericLoader, 'operations.GlobalWarmingCommitment')
etl.register(parsers.CampusEnergyWebsite, loader.GenericLoader, 'operations.EnergyWebsite')
etl.register(parsers.CampusEnergyPlan, loader.GenericLoader, 'operations.EnergyPlan')
etl.register(parsers.ElectricVehicleFleet, loader.GenericLoader, 'operations.ElectricFleet')
etl.register(parsers.CarBan, loader.CarBanLoader, 'operations.CarBan')
etl.register(parsers.BiodieselFleet, loader.BiodieselFleetLoader, 'operations.BiodieselFleet')
etl.register(parsers.BicyclePlans, loader.GenericLoader, 'operations.BicyclePlan')
etl.register(parsers.BuildingEnergyDashboard, loader.BuildingDashboardLoader, 'operations.BuildingDashboard')
etl.register(parsers.AlternativeTransport, loader.GenericLoader, 'operations.TransportationWebsite')
etl.register(parsers.BottledWaterBans, loader.BottleWaterBanLoader, 'operations.BottledWaterBan')
etl.register(parsers.CarSharing, loader.CarShareLoader, 'operations.CarShare')
etl.register(parsers.RecyclingWasteMinimization, loader.GenericLoader,
             'operations.RecyclingWebsite')
etl.register(parsers.ElectronicWasteEvents, loader.GenericLoader,
             'operations.ElectronicWasteEvent', reset=False)

# register education
etl.register(parsers.SustainableLivingGuide,
             loader.GenericLoader, 'education.LivingGuide', reset=True)
etl.register(parsers.CampusAgriculture, loader.GenericLoader,
             'education.CampusAgriculture', reset=True)
etl.register(parsers.SustainabilityResearchInventories,
             loader.GenericLoader, 'education.ResearchInventory', reset=True)
etl.register(parsers.SustainableCourseInventories,
             loader.GenericLoader, 'education.SustainabilityCourseInventory',
             reset=True)
etl.register(parsers.SustainabilitySyllabi, loader.GenericLoader,
             'education.SustainabilitySyllabus', reset=True)
etl.register(parsers.FacultyDevelopmentWorkshops,
             loader.GenericLoader, 'education.FacultyWorkshop', reset=True)
etl.register(parsers.SurveysAwarenessAttitudes, loader.GenericLoader,
             'education.SurveyOfAwareness', reset=True)
for academic_center_type in ('Agriculture', 'Architecture',
                             'Business', 'DevelopmentStudies',
                             'Economics', 'Education', 'Engineering',
                             'Law', 'UrbanStudies'):
    etl.register(getattr(parsers, ''.join(('AcademicCenters',
                    academic_center_type))),
                    loader.AcademicCenterLoader,
                    'education.AcademicCenter',
                    reset=True)
etl.register(parsers.education.CampusSustainabilityCourses,
             loader.CampusSustainabilityCourseLoader,
             'education.CampusSustainabilityCourse',
             reset=True)
etl.register(parsers.education.CampusGardens,
             loader.GenericLoader,
             'education.CommunityGarden',
             reset=True)
etl.register(parsers.education.SustainabilityNetworks,
             loader.GenericLoader,
             'education.SustainabilityNetwork',
             reset=True)
etl.register(parsers.education.SustainabilityMaps,
             loader.GenericLoader,
             'education.SustainabilityMap',
             reset=True)

# policies
etl.register(parsers.ApplianceProcurementPolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)
etl.register(parsers.AntiIdlingPolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)
etl.register(parsers.CampusFairTradePolicies, loader.PolicyLoader,
             'policies.FairTradePolicy', reset=False)
etl.register(parsers.ElectronicWastePolicies, loader.PolicyLoader,
             'policies.ElectronicWastePolicy', reset=False)
etl.register(parsers.EnergyConservationPolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)
etl.register(parsers.GeneralProcurementPolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)
etl.register(parsers.GeneralSustainabilityPolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)
etl.register(parsers.GreenBuildingPolicies, loader.PolicyLoader,
             'policies.GreenBuildingPolicy', reset=False)
etl.register(parsers.GreenCleaningPolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)
etl.register(parsers.IntegratedPestPolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)
etl.register(parsers.LicenseeCodeConductPolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)
etl.register(parsers.LivingWagePolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)
etl.register(parsers.PaperProcurementPolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)
etl.register(parsers.RecyclingPolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)
etl.register(parsers.ResponsibleInvestmentPolicies, loader.PolicyLoader,
             'policies.ResponsibleInvestmentPolicy', reset=False)
etl.register(parsers.StormwaterPolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)
etl.register(parsers.TelecommutingPolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)
etl.register(parsers.WaterConservationPolicies, loader.PolicyLoader,
             'policies.Policy', reset=False)

# register PAE
etl.register(parsers.AlumniSustainabilityFunds, loader.GenericLoader, 'pae.AlumniFund')
etl.register(parsers.CampusMasterPlan, loader.GenericLoader, 'pae.MasterPlan')
etl.register(parsers.AssessmentTools, loader.AssessmentToolsLoader, 'pae.AssessmentTool')
etl.register(parsers.SustainabilityBlog, loader.GenericLoader, 'pae.SustainabilityBlog')
etl.register(parsers.SustainabilityPlan, loader.GenericLoader, 'pae.SustainabilityPlan')
etl.register(parsers.RevolvingFund, loader.GenericLoader, 'pae.RevolvingLoanFund')

# programs
etl.register(parsers.BicycleSharePrograms, loader.ProgramLoader,
             'programs.Program')
etl.register(parsers.CampusCompostingPrograms, loader.ProgramLoader,
             'programs.Program')
etl.register(parsers.ElectronicWastePrograms, loader.ProgramLoader,
             'programs.ElectronicWasteProgram')
etl.register(parsers.StudentSustainabilityEducatorPrograms,
             loader.ProgramLoader, 'programs.Program')
etl.register(parsers.SurplusPropertyRecyclingPrograms, loader.ProgramLoader,
             'programs.Program')
etl.register(parsers.GreenCleaningPrograms, loader.ProgramLoader,
             'programs.Program')
etl.register(parsers.GreenOfficePrograms, loader.ProgramLoader,
             'programs.Program')
