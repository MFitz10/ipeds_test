from __future__ import unicode_literals

from django.contrib.gis.db import models


ETHNICITY_CHOICES = (
        ('aian', 'American Indian or Alaska Native'),
        ('asian', 'Asian'),
        ('black', 'Black or African American'),
        ('hispanic', 'Hispanic or Latino'),
        ('nhpi', 'Native Hawaiian or Other Pacific Islander'),
        ('white', 'White'),
        ('biracial', 'Two or More Races'),
        ('unknown', 'Race/Ethnicity Unknown'),
)

GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
)

CIPCODE_CHOICES = (
    (99.0,"Grand total"),
    (01.0000,"Agriculture, General"),
    (01.0101,"Agricultural Business and Management, General"),
    (01.0102,"Agribusiness/Agricultural Business Operations"),
    (01.0103,"Agricultural Economics"),
    (01.0104,"Farm/Farm and Ranch Management"),
    (01.0105,"Agricultural/Farm Supplies Retailing and Wholesaling"),
    (01.0106,"Agricultural Business Technology"),
    (01.0199,"Agricultural Business and Management, Other"),
    (01.0201,"Agricultural Mechanization, General"),
    (01.0204,"Agricultural Power Machinery Operation"),
    (01.0205,"Agricultural Mechanics and Equipment/Machine Technology"),
    (01.0299,"Agricultural Mechanization, Other"),
    (01.0301,"Agricultural Production Operations, General"),
    (01.0302,"Animal/Livestock Husbandry and Production"),
    (01.0303,"Aquaculture"),
    (01.0304,"Crop Production"),
    (01.0306,"Dairy Husbandry and Production"),
    (01.0307,"Horse Husbandry/Equine Science and Management"),
    (01.0308,"Agroecology and Sustainable Agriculture"),
    (01.0309,"Viticulture and Enology"),
    (01.0399,"Agricultural Production Operations, Other"),
    (01.0401,"Agricultural and Food Products Processing"),
    (01.0504,"Dog/Pet/Animal Grooming"),
    (01.0505,"Animal Training"),
    (01.0507,"Equestrian/Equine Studies"),
    (01.0508,"Taxidermy/Taxidermist"),
    (01.0599,"Agricultural and Domestic Animal Services, Other"),
    (01.0601,"Applied Horticulture/Horticulture Operations, General"),
    (01.0603,"Ornamental Horticulture"),
    (01.0604,"Greenhouse Operations and Management"),
    (01.0605,"Landscaping and Groundskeeping"),
    (01.0606,"Plant Nursery Operations and Management"),
    (01.0607,"Turf and Turfgrass Management"),
    (01.0608,"Floriculture/Floristry Operations and Management"),
    (01.0699,"Applied Horticulture/Horticultural Business Services, Other"),
    (01.0701,"International Agriculture"),
    (01.0801,"Agricultural and Extension Education Services"),
    (01.0802,"Agricultural Communication/Journalism"),
    (01.0899,"Agricultural Public Services, Other"),
    (01.0901,"Animal Sciences, General"),
    (01.0902,"Agricultural Animal Breeding"),
    (01.0903,"Animal Health"),
    (01.0904,"Animal Nutrition"),
    (01.0905,"Dairy Science"),
    (01.0906,"Livestock Management"),
    (01.0907,"Poultry Science"),
    (01.0999,"Animal Sciences, Other"),
    (01.1001,"Food Science"),
    (01.1002,"Food Technology and Processing"),
    (01.1099,"Food Science and Technology, Other"),
    (01.1101,"Plant Sciences, General"),
    (01.1102,"Agronomy and Crop Science"),
    (01.1103,"Horticultural Science"),
    (01.1104,"Agricultural and Horticultural Plant Breeding"),
    (01.1105,"Plant Protection and Integrated Pest Management"),
    (01.1106,"Range Science and Management"),
    (01.1199,"Plant Sciences, Other"),
    (01.1201,"Soil Science and Agronomy, General"),
    (01.1202,"Soil Chemistry and Physics"),
    (01.1299,"Soil Sciences, Other"),
    (01.9999,"Agriculture, Agriculture Operations and Related Sciences, Other"),
    (03.0101,"Natural Resources/Conservation, General"),
    (03.0103,"Environmental Studies"),
    (03.0104,"Environmental Science"),
    (03.0199,"Natural Resources Conservation and Research, Other"),
    (03.0201,"Natural Resources Management and Policy"),
    (03.0204,"Natural Resource Economics"),
    (03.0205,"Water, Wetlands, and Marine Resources Management"),
    (03.0206,"Land Use Planning and Management/Development"),
    (03.0207,"Natural Resource Recreation and Tourism"),
    (03.0208,"Natural Resources Law Enforcement and Protective Services"),
    (03.0299,"Natural Resources Management and Policy, Other"),
    (03.0301,"Fishing and Fisheries Sciences and Management"),
    (03.0501,"Forestry, General"),
    (03.0502,"Forest Sciences and Biology"),
    (03.0506,"Forest Management/Forest Resources Management"),
    (03.0508,"Urban Forestry"),
    (03.0509,"Wood Science and Wood Products/Pulp and Paper Technology"),
    (03.0510,"Forest Resources Production and Management"),
    (03.0511,"Forest Technology/Technician"),
    (03.0599,"Forestry, Other"),
    (03.0601,"Wildlife, Fish and Wildlands Science and Management"),
    (03.9999,"Natural Resources and Conservation, Other"),
    (04.0201,"Architecture"),
    (04.0301,"City/Urban, Community and Regional Planning"),
    (04.0401,"Environmental Design/Architecture"),
    (04.0501,"Interior Architecture"),
    (04.0601,"Landscape Architecture"),
    (04.0801,"Architectural History and Criticism, General"),
    (04.0901,"Architectural Technology/Technician"),
    (04.0902,"Architectural and Building Sciences/Technology"),
    (04.0999,"Architectural Sciences and Technology, Other"),
    (04.1001,"Real Estate Development"),
    (04.9999,"Architecture and Related Services, Other"),
    (05.0101,"African Studies"),
    (05.0102,"American/United States Studies/Civilization"),
    (05.0103,"Asian Studies/Civilization"),
    (05.0104,"East Asian Studies"),
    (05.0105,"Russian, Central European, East European and Eurasian Studies"),
    (05.0106,"European Studies/Civilization"),
    (05.0107,"Latin American Studies"),
    (05.0108,"Near and Middle Eastern Studies"),
    (05.0109,"Pacific Area/Pacific Rim Studies"),
    (05.0110,"Russian Studies"),
    (05.0111,"Scandinavian Studies"),
    (05.0112,"South Asian Studies"),
    (05.0113,"Southeast Asian Studies"),
    (05.0114,"Western European Studies"),
    (05.0115,"Canadian Studies"),
    (05.0118,"Slavic Studies"),
    (05.0119,"Caribbean Studies"),
    (05.0120,"Ural-Altaic and Central Asian Studies"),
    (05.0122,"Regional Studies (U.S., Canadian, Foreign)"),
    (05.0123,"Chinese Studies"),
    (05.0124,"French Studies"),
    (05.0125,"German Studies"),
    (05.0126,"Italian Studies"),
    (05.0127,"Japanese Studies"),
    (05.0128,"Korean Studies"),
    (05.0130,"Spanish and Iberian Studies"),
    (05.0131,"Tibetan Studies"),
    (05.0133,"Irish Studies"),
    (05.0134,"Latin American and Caribbean Studies"),
    (05.0199,"Area Studies, Other"),
    (05.0200,"Ethnic Studies"),
    (05.0201,"African-American/Black Studies"),
    (05.0202,"American Indian/Native American Studies"),
    (05.0203,"Hispanic-American, Puerto Rican, and Mexican-American/Chicano Studies"),
    (05.0206,"Asian-American Studies"),
    (05.0207,"Women's Studies"),
    (05.0208,"Gay/Lesbian Studies"),
    (05.0209,"Folklore Studies"),
    (05.0210,"Disability Studies"),
    (05.0211,"Deaf Studies"),
    (05.0299,"Ethnic, Cultural Minority, Gender, and Group Studies, Other"),
    (09.0100,"Communication, General"),
    (09.0101,"Speech Communication and Rhetoric"),
    (09.0102,"Mass Communication/Media Studies"),
    (09.0199,"Communication and Media Studies, Other"),
    (09.0401,"Journalism"),
    (09.0402,"Broadcast Journalism"),
    (09.0404,"Photojournalism"),
    (09.0499,"Journalism, Other"),
    (09.0701,"Radio and Television"),
    (09.0702,"Digital Communication and Media/Multimedia"),
    (09.0799,"Radio, Television, and Digital Communication, Other"),
    (09.0900,"Public Relations, Advertising, and Applied Communication"),
    (09.0901,"Organizational Communication, General"),
    (09.0902,"Public Relations/Image Management"),
    (09.0903,"Advertising"),
    (09.0904,"Political Communication"),
    (09.0905,"Health Communication"),
    (09.0906,"Sports Communication"),
    (09.0907,"International and Intercultural Communication"),
    (09.0908,"Technical and Scientific Communication"),
    (09.0999,"Public Relations, Advertising, and Applied Communication, Other"),
    (09.1001,"Publishing"),
    (09.9999,"Communication, Journalism, and Related Programs, Other"),
    (10.0105,"Communications Technology/Technician"),
    (10.0201,"Photographic and Film/Video Technology/Technician and Assistant"),
    (10.0202,"Radio and Television Broadcasting Technology/Technician"),
    (10.0203,"Recording Arts Technology/Technician"),
    (10.0299,"Audiovisual Communications Technologies/Technicians, Other"),
    (10.0301,"Graphic Communications, General"),
    (10.0302,"Printing Management"),
    (10.0303,"Prepress/Desktop Publishing and Digital Imaging Design"),
    (10.0304,"Animation, Interactive Technology, Video Graphics and Special Effects"),
    (10.0305,"Graphic and Printing Equipment Operator, General Production"),
    (10.0306,"Platemaker/Imager"),
    (10.0307,"Printing Press Operator"),
    (10.0308,"Computer Typography and Composition Equipment Operator"),
    (10.0399,"Graphic Communications, Other"),
    (10.9999,"Communications Technologies/Technicians and Support Services, Other"),
    (11.0101,"Computer and Information Sciences, General"),
    (11.0102,"Artificial Intelligence"),
    (11.0103,"Information Technology"),
    (11.0104,"Informatics"),
    (11.0199,"Computer and Information Sciences, Other"),
    (11.0201,"Computer Programming/Programmer, General"),
    (11.0202,"Computer Programming, Specific Applications"),
    (11.0203,"Computer Programming, Vendor/Product Certification"),
    (11.0299,"Computer Programming, Other"),
    (11.0301,"Data Processing and Data Processing Technology/Technician"),
    (11.0401,"Information Science/Studies"),
    (11.0501,"Computer Systems Analysis/Analyst"),
    (11.0601,"Data Entry/Microcomputer Applications, General"),
    (11.0602,"Word Processing"),
    (11.0699,"Data Entry/Microcomputer Applications, Other"),
    (11.0701,"Computer Science"),
    (11.0801,"Web Page, Digital/Multimedia and Information Resources Design"),
    (11.0802,"Data Modeling/Warehousing and Database Administration"),
    (11.0803,"Computer Graphics"),
    (11.0804,"Modeling, Virtual Environments and Simulation"),
    (11.0899,"Computer Software and Media Applications, Other"),
    (11.0901,"Computer Systems Networking and Telecommunications"),
    (11.1001,"Network and System Administration/Administrator"),
    (11.1002,"System, Networking, and LAN/WAN Management/Manager"),
    (11.1003,"Computer and Information Systems Security/Information Assurance"),
    (11.1004,"Web/Multimedia Management and Webmaster"),
    (11.1005,"Information Technology Project Management"),
    (11.1006,"Computer Support Specialist"),
    (11.1099,"Computer/Information Technology Services Administration and Management, Other"),
    (11.9999,"Computer and Information Sciences and Support Services, Other"),
    (12.0301,"Funeral Service and Mortuary Science, General"),
    (12.0302,"Funeral Direction/Service"),
    (12.0303,"Mortuary Science and Embalming/Embalmer"),
    (12.0399,"Funeral Service and Mortuary Science, Other"),
    (12.0401,"Cosmetology/Cosmetologist, General"),
    (12.0402,"Barbering/Barber"),
    (12.0404,"Electrolysis/Electrology and Electrolysis Technician"),
    (12.0406,"Make-Up Artist/Specialist"),
    (12.0407,"Hair Styling/Stylist and Hair Design"),
    (12.0408,"Facial Treatment Specialist/Facialist"),
    (12.0409,"Aesthetician/Esthetician and Skin Care Specialist"),
    (12.0410,"Nail Technician/Specialist and Manicurist"),
    (12.0411,"Permanent Cosmetics/Makeup and Tattooing"),
    (12.0412,"Salon/Beauty Salon Management/Manager"),
    (12.0413,"Cosmetology, Barber/Styling, and Nail Instructor"),
    (12.0414,"Master Aesthetician/Esthetician"),
    (12.0499,"Cosmetology and Related Personal Grooming Arts, Other"),
    (12.0500,"Cooking and Related Culinary Arts, General"),
    (12.0501,"Baking and Pastry Arts/Baker/Pastry Chef"),
    (12.0502,"Bartending/Bartender"),
    (12.0503,"Culinary Arts/Chef Training"),
    (12.0504,"Restaurant, Culinary, and Catering Management/Manager"),
    (12.0505,"Food Preparation/Professional Cooking/Kitchen Assistant"),
    (12.0506,"Meat Cutting/Meat Cutter"),
    (12.0507,"Food Service, Waiter/Waitress, and Dining Room Management/Manager"),
    (12.0508,"Institutional Food Workers"),
    (12.0509,"Culinary Science/Culinology"),
    (12.0510,"Wine Steward/Sommelier"),
    (12.0599,"Culinary Arts and Related Services, Other"),
    (12.9999,"Personal and Culinary Services, Other"),
    (13.0101,"Education, General"),
    (13.0201,"Bilingual and Multilingual Education"),
    (13.0202,"Multicultural Education"),
    (13.0203,"Indian/Native American Education"),
    (13.0299,"Bilingual, Multilingual, and Multicultural Education, Other"),
    (13.0301,"Curriculum and Instruction"),
    (13.0401,"Educational Leadership and Administration, General"),
    (13.0402,"Administration of Special Education"),
    (13.0403,"Adult and Continuing Education Administration"),
    (13.0404,"Educational, Instructional, and Curriculum Supervision"),
    (13.0406,"Higher Education/Higher Education Administration"),
    (13.0407,"Community College Education"),
    (13.0408,"Elementary and Middle School Administration/Principalship"),
    (13.0409,"Secondary School Administration/Principalship"),
    (13.0410,"Urban Education and Leadership"),
    (13.0411,"Superintendency and Educational System Administration"),
    (13.0499,"Educational Administration and Supervision, Other"),
    (13.0501,"Educational/Instructional Technology"),
    (13.0601,"Educational Evaluation and Research"),
    (13.0603,"Educational Statistics and Research Methods"),
    (13.0604,"Educational Assessment, Testing, and Measurement"),
    (13.0607,"Learning Sciences"),
    (13.0699,"Educational Assessment, Evaluation, and Research, Other"),
    (13.0701,"International and Comparative Education"),
    (13.0901,"Social and Philosophical Foundations of Education"),
    (13.1001,"Special Education and Teaching, General"),
    (13.1003,"Education/Teaching of Individuals with Hearing Impairments Including Deafness"),
    (13.1004,"Education/Teaching of the Gifted and Talented"),
    (13.1005,"Education/Teaching of Individuals with Emotional Disturbances"),
    (13.1006,"Education/Teaching of Individuals with Mental Retardation"),
    (13.1007,"Education/Teaching of Individuals with Multiple Disabilities"),
    (13.1008,"Education/Teaching of Individuals with Orthopedic and Other Physical Health Impa"),
    (13.1009,"Education/Teaching of Individuals with Vision Impairments Including Blindness"),
    (13.1011,"Education/Teaching of Individuals with Specific Learning Disabilities"),
    (13.1012,"Education/Teaching of Individuals with Speech or Language Impairments"),
    (13.1013,"Education/Teaching of Individuals with Autism"),
    (13.1014,"Education/Teaching of Individuals Who are Developmentally Delayed"),
    (13.1015,"Education/Teaching of Individuals in Early Childhood Special Education Programs"),
    (13.1017,"Education/Teaching of Individuals in Elementary Special Education Programs"),
    (13.1018,"Education/Teaching of Individuals in Junior High/Middle School Special Education"),
    (13.1019,"Education/Teaching of Individuals in Secondary Special Education Programs"),
    (13.1099,"Special Education and Teaching, Other"),
    (13.1101,"Counselor Education/School Counseling and Guidance Services"),
    (13.1102,"College Student Counseling and Personnel Services"),
    (13.1199,"Student Counseling and Personnel Services, Other"),
    (13.1201,"Adult and Continuing Education and Teaching"),
    (13.1202,"Elementary Education and Teaching"),
    (13.1203,"Junior High/Intermediate/Middle School Education and Teaching"),
    (13.1205,"Secondary Education and Teaching"),
    (13.1206,"Teacher Education, Multiple Levels"),
    (13.1207,"Montessori Teacher Education"),
    (13.1209,"Kindergarten/Preschool Education and Teaching"),
    (13.1210,"Early Childhood Education and Teaching"),
    (13.1299,"Teacher Education and Professional Development, Specific Levels and Methods, Oth"),
    (13.1301,"Agricultural Teacher Education"),
    (13.1302,"Art Teacher Education"),
    (13.1303,"Business Teacher Education"),
    (13.1304,"Driver and Safety Teacher Education"),
    (13.1305,"English/Language Arts Teacher Education"),
    (13.1306,"Foreign Language Teacher Education"),
    (13.1307,"Health Teacher Education"),
    (13.1308,"Family and Consumer Sciences/Home Economics Teacher Education"),
    (13.1309,"Technology Teacher Education/Industrial Arts Teacher Education"),
    (13.1310,"Sales and Marketing Operations/Marketing and Distribution Teacher Education"),
    (13.1311,"Mathematics Teacher Education"),
    (13.1312,"Music Teacher Education"),
    (13.1314,"Physical Education Teaching and Coaching"),
    (13.1315,"Reading Teacher Education"),
    (13.1316,"Science Teacher Education/General Science Teacher Education"),
    (13.1317,"Social Science Teacher Education"),
    (13.1318,"Social Studies Teacher Education"),
    (13.1319,"Technical Teacher Education"),
    (13.1320,"Trade and Industrial Teacher Education"),
    (13.1321,"Computer Teacher Education"),
    (13.1322,"Biology Teacher Education"),
    (13.1323,"Chemistry Teacher Education"),
    (13.1324,"Drama and Dance Teacher Education"),
    (13.1325,"French Language Teacher Education"),
    (13.1326,"German Language Teacher Education"),
    (13.1327,"Health Occupations Teacher Education"),
    (13.1328,"History Teacher Education"),
    (13.1329,"Physics Teacher Education"),
    (13.1330,"Spanish Language Teacher Education"),
    (13.1331,"Speech Teacher Education"),
    (13.1332,"Geography Teacher Education"),
    (13.1333,"Latin Teacher Education"),
    (13.1334,"School Librarian/School Library Media Specialist"),
    (13.1335,"Psychology Teacher Education"),
    (13.1337,"Earth Science Teacher Education"),
    (13.1338,"Environmental Education"),
    (13.1399,"Teacher Education and Professional Development, Specific Subject Areas, Other"),
    (13.1401,"Teaching English as a Second or Foreign Language/ESL Language Instructor"),
    (13.1402,"Teaching French as a Second or Foreign Language"),
    (13.1499,"Teaching English or French as a Second or Foreign Language, Other"),
    (13.1501,"Teacher Assistant/Aide"),
    (13.1502,"Adult Literacy Tutor/Instructor"),
    (13.1599,"Teaching Assistants/Aides, Other"),
    (13.9999,"Education, Other"),
    (14.0101,"Engineering, General"),
    (14.0102,"Pre-Engineering"),
    (14.0201,"Aerospace, Aeronautical and Astronautical/Space Engineering"),
    (14.0301,"Agricultural Engineering"),
    (14.0401,"Architectural Engineering"),
    (14.0501,"Bioengineering and Biomedical Engineering"),
    (14.0601,"Ceramic Sciences and Engineering"),
    (14.0701,"Chemical Engineering"),
    (14.0702,"Chemical and Biomolecular Engineering"),
    (14.0799,"Chemical Engineering, Other"),
    (14.0801,"Civil Engineering, General"),
    (14.0802,"Geotechnical and Geoenvironmental Engineering"),
    (14.0803,"Structural Engineering"),
    (14.0804,"Transportation and Highway Engineering"),
    (14.0805,"Water Resources Engineering"),
    (14.0899,"Civil Engineering, Other"),
    (14.0901,"Computer Engineering, General"),
    (14.0902,"Computer Hardware Engineering"),
    (14.0903,"Computer Software Engineering"),
    (14.0999,"Computer Engineering, Other"),
    (14.1001,"Electrical and Electronics Engineering"),
    (14.1003,"Laser and Optical Engineering"),
    (14.1004,"Telecommunications Engineering"),
    (14.1099,"Electrical, Electronics and Communications Engineering, Other"),
    (14.1101,"Engineering Mechanics"),
    (14.1201,"Engineering Physics/Applied Physics"),
    (14.1301,"Engineering Science"),
    (14.1401,"Environmental/Environmental Health Engineering"),
    (14.1801,"Materials Engineering"),
    (14.1901,"Mechanical Engineering"),
    (14.2001,"Metallurgical Engineering"),
    (14.2101,"Mining and Mineral Engineering"),
    (14.2201,"Naval Architecture and Marine Engineering"),
    (14.2301,"Nuclear Engineering"),
    (14.2401,"Ocean Engineering"),
    (14.2501,"Petroleum Engineering"),
    (14.2701,"Systems Engineering"),
    (14.2801,"Textile Sciences and Engineering"),
    (14.3201,"Polymer/Plastics Engineering"),
    (14.3301,"Construction Engineering"),
    (14.3401,"Forest Engineering"),
    (14.3501,"Industrial Engineering"),
    (14.3601,"Manufacturing Engineering"),
    (14.3701,"Operations Research"),
    (14.3801,"Surveying Engineering"),
    (14.3901,"Geological/Geophysical Engineering"),
    (14.4001,"Paper Science and Engineering"),
    (14.4101,"Electromechanical Engineering"),
    (14.4201,"Mechatronics, Robotics, and Automation Engineering"),
    (14.4301,"Biochemical Engineering"),
    (14.4401,"Engineering Chemistry"),
    (14.4501,"Biological/Biosystems Engineering"),
    (14.9999,"Engineering, Other"),
    (15.0000,"Engineering Technology, General"),
    (15.0101,"Architectural Engineering Technology/Technician"),
    (15.0201,"Civil Engineering Technology/Technician"),
    (15.0303,"Electrical, Electronic and Communications Engineering Technology/Technician"),
    (15.0304,"Laser and Optical Technology/Technician"),
    (15.0305,"Telecommunications Technology/Technician"),
    (15.0306,"Integrated Circuit Design"),
    (15.0399,"Electrical and Electronic Engineering Technologies/Technicians, Other"),
    (15.0401,"Biomedical Technology/Technician"),
    (15.0403,"Electromechanical Technology/Electromechanical Engineering Technology"),
    (15.0404,"Instrumentation Technology/Technician"),
    (15.0405,"Robotics Technology/Technician"),
    (15.0406,"Automation Engineer Technology/Technician"),
    (15.0499,"Electromechanical and Instrumentation and Maintenance Technologies/Technicians,"),
    (15.0501,"Heating, Ventilation, Air Conditioning and Refrigeration Engineering Technology/"),
    (15.0503,"Energy Management and Systems Technology/Technician"),
    (15.0505,"Solar Energy Technology/Technician"),
    (15.0506,"Water Quality and Wastewater Treatment Management and Recycling Technology/Techn"),
    (15.0507,"Environmental Engineering Technology/Environmental Technology"),
    (15.0508,"Hazardous Materials Management and Waste Technology/Technician"),
    (15.0599,"Environmental Control Technologies/Technicians, Other"),
    (15.0607,"Plastics and Polymer Engineering Technology/Technician"),
    (15.0611,"Metallurgical Technology/Technician"),
    (15.0612,"Industrial Technology/Technician"),
    (15.0613,"Manufacturing Engineering Technology/Technician"),
    (15.0614,"Welding Engineering Technology/Technician"),
    (15.0615,"Chemical Engineering Technology/Technician"),
    (15.0616,"Semiconductor Manufacturing Technology"),
    (15.0699,"Industrial Production Technologies/Technicians, Other"),
    (15.0701,"Occupational Safety and Health Technology/Technician"),
    (15.0702,"Quality Control Technology/Technician"),
    (15.0703,"Industrial Safety Technology/Technician"),
    (15.0799,"Quality Control and Safety Technologies/Technicians, Other"),
    (15.0801,"Aeronautical/Aerospace Engineering Technology/Technician"),
    (15.0803,"Automotive Engineering Technology/Technician"),
    (15.0805,"Mechanical Engineering/Mechanical Technology/Technician"),
    (15.0899,"Mechanical Engineering Related Technologies/Technicians, Other"),
    (15.0901,"Mining Technology/Technician"),
    (15.0903,"Petroleum Technology/Technician"),
    (15.0999,"Mining and Petroleum Technologies/Technicians, Other"),
    (15.1001,"Construction Engineering Technology/Technician"),
    (15.1102,"Surveying Technology/Surveying"),
    (15.1103,"Hydraulics and Fluid Power Technology/Technician"),
    (15.1199,"Engineering-Related Technologies, Other"),
    (15.1201,"Computer Engineering Technology/Technician"),
    (15.1202,"Computer Technology/Computer Systems Technology"),
    (15.1203,"Computer Hardware Technology/Technician"),
    (15.1204,"Computer Software Technology/Technician"),
    (15.1299,"Computer Engineering Technologies/Technicians, Other"),
    (15.1301,"Drafting and Design Technology/Technician, General"),
    (15.1302,"CAD/CADD Drafting and/or Design Technology/Technician"),
    (15.1303,"Architectural Drafting and Architectural CAD/CADD"),
    (15.1304,"Civil Drafting and Civil Engineering CAD/CADD"),
    (15.1305,"Electrical/Electronics Drafting and Electrical/Electronics CAD/CADD"),
    (15.1306,"Mechanical Drafting and Mechanical Drafting CAD/CADD"),
    (15.1399,"Drafting/Design Engineering Technologies/Technicians, Other"),
    (15.1401,"Nuclear Engineering Technology/Technician"),
    (15.1501,"Engineering/Industrial Management"),
    (15.1502,"Engineering Design"),
    (15.1503,"Packaging Science"),
    (15.1599,"Engineering-Related Fields, Other"),
    (15.1601,"Nanotechnology"),
    (15.9999,"Engineering Technologies and Engineering-Related Fields, Other"),
    (16.0101,"Foreign Languages and Literatures, General"),
    (16.0102,"Linguistics"),
    (16.0103,"Language Interpretation and Translation"),
    (16.0104,"Comparative Literature"),
    (16.0105,"Applied Linguistics"),
    (16.0199,"Linguistic, Comparative, and Related Language Studies and Services, Other"),
    (16.0201,"African Languages, Literatures, and Linguistics"),
    (16.0300,"East Asian Languages, Literatures, and Linguistics, General"),
    (16.0301,"Chinese Language and Literature"),
    (16.0302,"Japanese Language and Literature"),
    (16.0303,"Korean Language and Literature"),
    (16.0399,"East Asian Languages, Literatures, and Linguistics, Other"),
    (16.0400,"Slavic Languages, Literatures, and Linguistics, General"),
    (16.0402,"Russian Language and Literature"),
    (16.0406,"Czech Language and Literature"),
    (16.0407,"Polish Language and Literature"),
    (16.0408,"Bosnian, Serbian, and Croatian Languages and Literatures"),
    (16.0499,"Slavic, Baltic, and Albanian Languages, Literatures, and Linguistics, Other"),
    (16.0500,"Germanic Languages, Literatures, and Linguistics, General"),
    (16.0501,"German Language and Literature"),
    (16.0502,"Scandinavian Languages, Literatures, and Linguistics"),
    (16.0503,"Danish Language and Literature"),
    (16.0504,"Dutch/Flemish Language and Literature"),
    (16.0505,"Norwegian Language and Literature"),
    (16.0506,"Swedish Language and Literature"),
    (16.0599,"Germanic Languages, Literatures, and Linguistics, Other"),
    (16.0601,"Modern Greek Language and Literature"),
    (16.0700,"South Asian Languages, Literatures, and Linguistics, General"),
    (16.0702,"Sanskrit and Classical Indian Languages, Literatures, and Linguistics"),
    (16.0801,"Iranian Languages, Literatures, and Linguistics"),
    (16.0900,"Romance Languages, Literatures, and Linguistics, General"),
    (16.0901,"French Language and Literature"),
    (16.0902,"Italian Language and Literature"),
    (16.0904,"Portuguese Language and Literature"),
    (16.0905,"Spanish Language and Literature"),
    (16.0908,"Hispanic and Latin American Languages, Literatures, and Linguistics, General"),
    (16.0999,"Romance Languages, Literatures, and Linguistics, Other"),
    (16.1001,"American Indian/Native American Languages, Literatures, and Linguistics"),
    (16.1100,"Middle/Near Eastern and Semitic Languages, Literatures, and Linguistics, General"),
    (16.1101,"Arabic Language and Literature"),
    (16.1102,"Hebrew Language and Literature"),
    (16.1103,"Ancient Near Eastern and Biblical Languages, Literatures, and Linguistics"),
    (16.1199,"Middle/Near Eastern and Semitic Languages, Literatures, and Linguistics, Other"),
    (16.1200,"Classics and Classical Languages, Literatures, and Linguistics, General"),
    (16.1202,"Ancient/Classical Greek Language and Literature"),
    (16.1203,"Latin Language and Literature"),
    (16.1299,"Classics and Classical Languages, Literatures, and Linguistics, Other"),
    (16.1301,"Celtic Languages, Literatures, and Linguistics"),
    (16.1404,"Filipino/Tagalog Language and Literature"),
    (16.1408,"Vietnamese Language and Literature"),
    (16.1501,"Turkish Language and Literature"),
    (16.1502,"Uralic Languages, Literatures, and Linguistics"),
    (16.1601,"American Sign Language (ASL)"),
    (16.1602,"Linguistics of ASL and Other Sign Languages"),
    (16.1603,"Sign Language Interpretation and Translation"),
    (16.1699,"American Sign Language, Other"),
    (16.9999,"Foreign Languages, Literatures, and Linguistics, Other"),
    (19.0000,"Work and Family Studies"),
    (19.0101,"Family and Consumer Sciences/Human Sciences, General"),
    (19.0201,"Business Family and Consumer Sciences/Human Sciences"),
    (19.0202,"Family and Consumer Sciences/Human Sciences Communication"),
    (19.0203,"Consumer Merchandising/Retailing Management"),
    (19.0299,"Family and Consumer Sciences/Human Sciences Business Services, Other"),
    (19.0401,"Family Resource Management Studies, General"),
    (19.0402,"Consumer Economics"),
    (19.0403,"Consumer Services and Advocacy"),
    (19.0499,"Family and Consumer Economics and Related Services, Other"),
    (19.0501,"Foods, Nutrition, and Wellness Studies, General"),
    (19.0504,"Human Nutrition"),
    (19.0505,"Foodservice Systems Administration/Management"),
    (19.0599,"Foods, Nutrition, and Related Services, Other"),
    (19.0601,"Housing and Human Environments, General"),
    (19.0604,"Facilities Planning and Management"),
    (19.0699,"Housing and Human Environments, Other"),
    (19.0701,"Human Development and Family Studies, General"),
    (19.0702,"Adult Development and Aging"),
    (19.0704,"Family Systems"),
    (19.0706,"Child Development"),
    (19.0707,"Family and Community Services"),
    (19.0708,"Child Care and Support Services Management"),
    (19.0709,"Child Care Provider/Assistant"),
    (19.0710,"Developmental Services Worker"),
    (19.0799,"Human Development, Family Studies, and Related Services, Other"),
    (19.0901,"Apparel and Textiles, General"),
    (19.0902,"Apparel and Textile Manufacture"),
    (19.0904,"Textile Science"),
    (19.0905,"Apparel and Textile Marketing Management"),
    (19.0906,"Fashion and Fabric Consultant"),
    (19.0999,"Apparel and Textiles, Other"),
    (19.9999,"Family and Consumer Sciences/Human Sciences, Other"),
    (22.0000,"Legal Studies, General"),
    (22.0001,"Pre-Law Studies"),
    (22.0101,"Law"),
    (22.0201,"Advanced Legal Research/Studies, General"),
    (22.0202,"Programs for Foreign Lawyers"),
    (22.0203,"American/U.S. Law/Legal Studies/Jurisprudence"),
    (22.0205,"Banking, Corporate, Finance, and Securities Law"),
    (22.0206,"Comparative Law"),
    (22.0207,"Energy, Environment, and Natural Resources Law"),
    (22.0208,"Health Law"),
    (22.0209,"International Law and Legal Studies"),
    (22.0210,"International Business, Trade, and Tax Law"),
    (22.0211,"Tax Law/Taxation"),
    (22.0212,"Intellectual Property Law"),
    (22.0299,"Legal Research and Advanced Professional Studies, Other"),
    (22.0301,"Legal Administrative Assistant/Secretary"),
    (22.0302,"Legal Assistant/Paralegal"),
    (22.0303,"Court Reporting/Court Reporter"),
    (22.0399,"Legal Support Services, Other"),
    (22.9999,"Legal Professions and Studies, Other"),
    (23.0101,"English Language and Literature, General"),
    (23.1301,"Writing, General"),
    (23.1302,"Creative Writing"),
    (23.1303,"Professional, Technical, Business, and Scientific Writing"),
    (23.1304,"Rhetoric and Composition"),
    (23.1399,"Rhetoric and Composition/Writing Studies, Other"),
    (23.1401,"General Literature"),
    (23.1402,"American Literature (United States"),
    (23.1404,"English Literature (British and Commonwealth"),
    (23.1405,"Children's and Adolescent Literature"),
    (23.1499,"Literature, Other"),
    (23.9999,"English Language and Literature/Letters, Other"),
    (24.0101,"Liberal Arts and Sciences/Liberal Studies"),
    (24.0102,"General Studies"),
    (24.0103,"Humanities/Humanistic Studies"),
    (24.0199,"Liberal Arts and Sciences, General Studies and Humanities, Other"),
    (25.0101,"Library and Information Science"),
    (25.0103,"Archives/Archival Administration"),
    (25.0301,"Library and Archives Assisting"),
    (25.9999,"Library Science, Other"),
    (26.0101,"Biology/Biological Sciences, General"),
    (26.0102,"Biomedical Sciences, General"),
    (26.0202,"Biochemistry"),
    (26.0203,"Biophysics"),
    (26.0204,"Molecular Biology"),
    (26.0205,"Molecular Biochemistry"),
    (26.0206,"Molecular Biophysics"),
    (26.0207,"Structural Biology"),
    (26.0209,"Radiation Biology/Radiobiology"),
    (26.0210,"Biochemistry and Molecular Biology"),
    (26.0299,"Biochemistry, Biophysics and Molecular Biology, Other"),
    (26.0301,"Botany/Plant Biology"),
    (26.0305,"Plant Pathology/Phytopathology"),
    (26.0307,"Plant Physiology"),
    (26.0308,"Plant Molecular Biology"),
    (26.0399,"Botany/Plant Biology, Other"),
    (26.0401,"Cell/Cellular Biology and Histology"),
    (26.0403,"Anatomy"),
    (26.0404,"Developmental Biology and Embryology"),
    (26.0406,"Cell/Cellular and Molecular Biology"),
    (26.0407,"Cell Biology and Anatomy"),
    (26.0499,"Cell/Cellular Biology and Anatomical Sciences, Other"),
    (26.0502,"Microbiology, General"),
    (26.0503,"Medical Microbiology and Bacteriology"),
    (26.0504,"Virology"),
    (26.0505,"Parasitology"),
    (26.0507,"Immunology"),
    (26.0508,"Microbiology and Immunology"),
    (26.0599,"Microbiological Sciences and Immunology, Other"),
    (26.0701,"Zoology/Animal Biology"),
    (26.0702,"Entomology"),
    (26.0707,"Animal Physiology"),
    (26.0708,"Animal Behavior and Ethology"),
    (26.0709,"Wildlife Biology"),
    (26.0799,"Zoology/Animal Biology, Other"),
    (26.0801,"Genetics, General"),
    (26.0802,"Molecular Genetics"),
    (26.0804,"Animal Genetics"),
    (26.0805,"Plant Genetics"),
    (26.0806,"Human/Medical Genetics"),
    (26.0807,"Genome Sciences/Genomics"),
    (26.0899,"Genetics, Other"),
    (26.0901,"Physiology, General"),
    (26.0902,"Molecular Physiology"),
    (26.0903,"Cell Physiology"),
    (26.0904,"Endocrinology"),
    (26.0905,"Reproductive Biology"),
    (26.0907,"Cardiovascular Science"),
    (26.0908,"Exercise Physiology"),
    (26.0909,"Vision Science/Physiological Optics"),
    (26.0910,"Pathology/Experimental Pathology"),
    (26.0911,"Oncology and Cancer Biology"),
    (26.0999,"Physiology, Pathology, and Related Sciences, Other"),
    (26.1001,"Pharmacology"),
    (26.1002,"Molecular Pharmacology"),
    (26.1003,"Neuropharmacology"),
    (26.1004,"Toxicology"),
    (26.1005,"Molecular Toxicology"),
    (26.1006,"Environmental Toxicology"),
    (26.1007,"Pharmacology and Toxicology"),
    (26.1099,"Pharmacology and Toxicology, Other"),
    (26.1101,"Biometry/Biometrics"),
    (26.1102,"Biostatistics"),
    (26.1103,"Bioinformatics"),
    (26.1104,"Computational Biology"),
    (26.1199,"Biomathematics, Bioinformatics, and Computational Biology, Other"),
    (26.1201,"Biotechnology"),
    (26.1301,"Ecology"),
    (26.1302,"Marine Biology and Biological Oceanography"),
    (26.1303,"Evolutionary Biology"),
    (26.1304,"Aquatic Biology/Limnology"),
    (26.1305,"Environmental Biology"),
    (26.1306,"Population Biology"),
    (26.1307,"Conservation Biology"),
    (26.1308,"Systematic Biology/Biological Systematics"),
    (26.1309,"Epidemiology"),
    (26.1310,"Ecology and Evolutionary Biology"),
    (26.1399,"Ecology, Evolution, Systematics and Population Biology, Other"),
    (26.1401,"Molecular Medicine"),
    (26.1501,"Neuroscience"),
    (26.1502,"Neuroanatomy"),
    (26.1503,"Neurobiology and Anatomy"),
    (26.1504,"Neurobiology and Behavior"),
    (26.1599,"Neurobiology and Neurosciences, Other"),
    (26.9999,"Biological and Biomedical Sciences, Other"),
    (27.0101,"Mathematics, General"),
    (27.0102,"Algebra and Number Theory"),
    (27.0103,"Analysis and Functional Analysis"),
    (27.0105,"Topology and Foundations"),
    (27.0199,"Mathematics, Other"),
    (27.0301,"Applied Mathematics, General"),
    (27.0303,"Computational Mathematics"),
    (27.0304,"Computational and Applied Mathematics"),
    (27.0305,"Financial Mathematics"),
    (27.0306,"Mathematical Biology"),
    (27.0399,"Applied Mathematics, Other"),
    (27.0501,"Statistics, General"),
    (27.0502,"Mathematical Statistics and Probability"),
    (27.0503,"Mathematics and Statistics"),
    (27.0599,"Statistics, Other"),
    (27.9999,"Mathematics and Statistics, Other"),
    (29.0201,"Intelligence, General"),
    (29.0202,"Strategic Intelligence"),
    (29.0203,"Signal/Geospatial Intelligence"),
    (29.0204,"Command & Control (C3, C4I Systems and Operations)"),
    (29.0206,"Information/Psychological Warfare and Military Media Relations"),
    (29.0207,"Cyber/Electronic Operations and Warfare"),
    (29.0299,"Intelligence, Command Control and Information Operations, Other"),
    (29.0301,"Combat Systems Engineering"),
    (29.0303,"Engineering Acoustics"),
    (29.0307,"Undersea Warfare"),
    (29.0399,"Military Applied Sciences, Other"),
    (29.0402,"Air and Space Operations Technology"),
    (29.0404,"Explosive Ordinance/Bomb Disposal"),
    (29.0405,"Joint Command/Task Force (C3, C4I Systems)"),
    (29.0408,"Munitions Systems/Ordinance Technology"),
    (29.0499,"Military Systems and Maintenance Technology, Other"),
    (29.9999,"Military Technologies and Applied Sciences, Other"),
    (30.0000,"Multi-/Interdisciplinary Studies, General"),
    (30.0101,"Biological and Physical Sciences"),
    (30.0501,"Peace Studies and Conflict Resolution"),
    (30.0601,"Systems Science and Theory"),
    (30.0801,"Mathematics and Computer Science"),
    (30.1001,"Biopsychology"),
    (30.1101,"Gerontology"),
    (30.1201,"Historic Preservation and Conservation"),
    (30.1202,"Cultural Resource Management and Policy Analysis"),
    (30.1299,"Historic Preservation and Conservation, Other"),
    (30.1301,"Medieval and Renaissance Studies"),
    (30.1401,"Museology/Museum Studies"),
    (30.1501,"Science, Technology and Society"),
    (30.1601,"Accounting and Computer Science"),
    (30.1701,"Behavioral Sciences"),
    (30.1801,"Natural Sciences"),
    (30.1901,"Nutrition Sciences"),
    (30.2001,"International/Global Studies"),
    (30.2101,"Holocaust and Related Studies"),
    (30.2201,"Ancient Studies/Civilization"),
    (30.2202,"Classical, Ancient Mediterranean and Near Eastern Studies and Archaeology"),
    (30.2301,"Intercultural/Multicultural and Diversity Studies"),
    (30.2501,"Cognitive Science"),
    (30.2601,"Cultural Studies/Critical Theory and Analysis"),
    (30.2701,"Human Biology"),
    (30.2801,"Dispute Resolution"),
    (30.2901,"Maritime Studies"),
    (30.3001,"Computational Science"),
    (30.3101,"Human Computer Interaction"),
    (30.3201,"Marine Sciences"),
    (30.3301,"Sustainability Studies"),
    (30.9999,"Multi-/Interdisciplinary Studies, Other"),
    (31.0101,"Parks, Recreation and Leisure Studies"),
    (31.0301,"Parks, Recreation and Leisure Facilities Management, General"),
    (31.0302,"Golf Course Operation and Grounds Management"),
    (31.0399,"Parks, Recreation and Leisure Facilities Management, Other"),
    (31.0501,"Health and Physical Education/Fitness, General"),
    (31.0504,"Sport and Fitness Administration/Management"),
    (31.0505,"Kinesiology and Exercise Science"),
    (31.0507,"Physical Fitness Technician"),
    (31.0508,"Sports Studies"),
    (31.0599,"Health and Physical Education/Fitness, Other"),
    (31.0601,"Outdoor Education"),
    (31.9999,"Parks, Recreation, Leisure, and Fitness Studies, Other"),
    (38.0001,"Philosophy and Religious Studies, General"),
    (38.0101,"Philosophy"),
    (38.0102,"Logic"),
    (38.0103,"Ethics"),
    (38.0104,"Applied and Professional Ethics"),
    (38.0199,"Philosophy, Other"),
    (38.0201,"Religion/Religious Studies"),
    (38.0202,"Buddhist Studies"),
    (38.0203,"Christian Studies"),
    (38.0205,"Islamic Studies"),
    (38.0206,"Jewish/Judaic Studies"),
    (38.0299,"Religion/Religious Studies, Other"),
    (38.9999,"Philosophy and Religious Studies, Other"),
    (39.0201,"Bible/Biblical Studies"),
    (39.0301,"Missions/Missionary Studies and Missiology"),
    (39.0401,"Religious Education"),
    (39.0501,"Religious/Sacred Music"),
    (39.0601,"Theology/Theological Studies"),
    (39.0602,"Divinity/Ministry"),
    (39.0604,"Pre-Theology/Pre-Ministerial Studies"),
    (39.0605,"Rabbinical Studies"),
    (39.0606,"Talmudic Studies"),
    (39.0699,"Theological and Ministerial Studies, Other"),
    (39.0701,"Pastoral Studies/Counseling"),
    (39.0702,"Youth Ministry"),
    (39.0703,"Urban Ministry"),
    (39.0704,"Women's Ministry"),
    (39.0705,"Lay Ministry"),
    (39.0799,"Pastoral Counseling and Specialized Ministries, Other"),
    (39.9999,"Theology and Religious Vocations, Other"),
    (40.0101,"Physical Sciences"),
    (40.0201,"Astronomy"),
    (40.0202,"Astrophysics"),
    (40.0203,"Planetary Astronomy and Science"),
    (40.0299,"Astronomy and Astrophysics, Other"),
    (40.0401,"Atmospheric Sciences and Meteorology, General"),
    (40.0403,"Atmospheric Physics and Dynamics"),
    (40.0404,"Meteorology"),
    (40.0499,"Atmospheric Sciences and Meteorology, Other"),
    (40.0501,"Chemistry, General"),
    (40.0502,"Analytical Chemistry"),
    (40.0503,"Inorganic Chemistry"),
    (40.0504,"Organic Chemistry"),
    (40.0506,"Physical Chemistry"),
    (40.0507,"Polymer Chemistry"),
    (40.0508,"Chemical Physics"),
    (40.0509,"Environmental Chemistry"),
    (40.0510,"Forensic Chemistry"),
    (40.0511,"Theoretical Chemistry"),
    (40.0599,"Chemistry, Other"),
    (40.0601,"Geology/Earth Science, General"),
    (40.0602,"Geochemistry"),
    (40.0603,"Geophysics and Seismology"),
    (40.0604,"Paleontology"),
    (40.0605,"Hydrology and Water Resources Science"),
    (40.0607,"Oceanography, Chemical and Physical"),
    (40.0699,"Geological and Earth Sciences/Geosciences, Other"),
    (40.0801,"Physics, General"),
    (40.0802,"Atomic/Molecular Physics"),
    (40.0804,"Elementary Particle Physics"),
    (40.0806,"Nuclear Physics"),
    (40.0807,"Optics/Optical Sciences"),
    (40.0808,"Condensed Matter and Materials Physics"),
    (40.0809,"Acoustics"),
    (40.0810,"Theoretical and Mathematical Physics"),
    (40.0899,"Physics, Other"),
    (40.1001,"Materials Science"),
    (40.1002,"Materials Chemistry"),
    (40.9999,"Physical Sciences, Other"),
    (40.1099,"Materials Sciences, Other"),
    (41.0000,"Science Technologies/Technicians, General"),
    (41.0101,"Biology Technician/Biotechnology Laboratory Technician"),
    (41.0204,"Industrial Radiologic Technology/Technician"),
    (41.0205,"Nuclear/Nuclear Power Technology/Technician"),
    (41.0299,"Nuclear and Industrial Radiologic Technologies/Technicians, Other"),
    (41.0301,"Chemical Technology/Technician"),
    (41.0303,"Chemical Process Technology"),
    (41.0399,"Physical Science Technologies/Technicians, Other"),
    (41.9999,"Science Technologies/Technicians, Other"),
    (42.0101,"Psychology, General"),
    (42.2701,"Cognitive Psychology and Psycholinguistics"),
    (42.2702,"Comparative Psychology"),
    (42.2703,"Developmental and Child Psychology"),
    (42.2704,"Experimental Psychology"),
    (42.2705,"Personality Psychology"),
    (42.2706,"Physiological Psychology/Psychobiology"),
    (42.2707,"Social Psychology"),
    (42.2708,"Psychometrics and Quantitative Psychology"),
    (42.2709,"Psychopharmacology"),
    (42.2799,"Research and Experimental Psychology, Other"),
    (42.2801,"Clinical Psychology"),
    (42.2802,"Community Psychology"),
    (42.2803,"Counseling Psychology"),
    (42.2804,"Industrial and Organizational Psychology"),
    (42.2805,"School Psychology"),
    (42.2806,"Educational Psychology"),
    (42.2807,"Clinical Child Psychology"),
    (42.2808,"Environmental Psychology"),
    (42.2809,"Geropsychology"),
    (42.2810,"Health/Medical Psychology"),
    (42.2811,"Family Psychology"),
    (42.2812,"Forensic Psychology"),
    (42.2813,"Applied Psychology"),
    (42.2814,"Applied Behavior Analysis"),
    (42.2899,"Clinical, Counseling and Applied Psychology, Other"),
    (42.9999,"Psychology, Other"),
    (43.0102,"Corrections"),
    (43.0103,"Criminal Justice/Law Enforcement Administration"),
    (43.0104,"Criminal Justice/Safety Studies"),
    (43.0106,"Forensic Science and Technology"),
    (43.0107,"Criminal Justice/Police Science"),
    (43.0109,"Security and Loss Prevention Services"),
    (43.0110,"Juvenile Corrections"),
    (43.0111,"Criminalistics and Criminal Science"),
    (43.0112,"Securities Services Administration/Management"),
    (43.0113,"Corrections Administration"),
    (43.0114,"Law Enforcement Investigation and Interviewing"),
    (43.0115,"Law Enforcement Record-Keeping and Evidence Management"),
    (43.0116,"Cyber/Computer Forensics and Counterterrorism"),
    (43.0117,"Financial Forensics and Fraud Investigation"),
    (43.0118,"Law Enforcement Intelligence Analysis"),
    (43.0119,"Critical Incident Response/Special Police Operations"),
    (43.0120,"Protective Services Operations"),
    (43.0199,"Corrections and Criminal Justice, Other"),
    (43.0201,"Fire Prevention and Safety Technology/Technician"),
    (43.0202,"Fire Services Administration"),
    (43.0203,"Fire Science/Fire-fighting"),
    (43.0204,"Fire Systems Technology"),
    (43.0205,"Fire/Arson Investigation and Prevention"),
    (43.0206,"Wildland/Forest Firefighting and Investigation"),
    (43.0299,"Fire Protection, Other"),
    (43.0301,"Homeland Security"),
    (43.0302,"Crisis/Emergency/Disaster Management"),
    (43.0303,"Critical Infrastructure Protection"),
    (43.0304,"Terrorism and Counterterrorism Operations"),
    (43.0399,"Homeland Security, Other"),
    (43.9999,"Homeland Security, Law Enforcement, Firefighting and Related Protective Services, Other"),
    (44.0000,"Human Services, General"),
    (44.0201,"Community Organization and Advocacy"),
    (44.0401,"Public Administration"),
    (44.0501,"Public Policy Analysis, General"),
    (44.0502,"Education Policy Analysis"),
    (44.0503,"Health Policy Analysis"),
    (44.0504,"International Policy Analysis"),
    (44.0599,"Public Policy Analysis, Other"),
    (44.0701,"Social Work"),
    (44.0702,"Youth Services/Administration"),
    (44.0799,"Social Work, Other"),
    (44.9999,"Public Administration and Social Service Professions, Other"),
    (45.0101,"Social Sciences, General"),
    (45.0102,"Research Methodology and Quantitative Methods"),
    (45.0201,"Anthropology"),
    (45.0202,"Physical and Biological Anthropology"),
    (45.0204,"Cultural Anthropology"),
    (45.0299,"Anthropology, Other"),
    (45.0301,"Archeology"),
    (45.0401,"Criminology"),
    (45.0501,"Demography and Population Studies"),
    (45.0601,"Economics, General"),
    (45.0602,"Applied Economics"),
    (45.0603,"Econometrics and Quantitative Economics"),
    (45.0604,"Development Economics and International Development"),
    (45.0605,"International Economics"),
    (45.0699,"Economics, Other"),
    (45.0701,"Geography"),
    (45.0702,"Geographic Information Science and Cartography"),
    (45.0799,"Geography, Other"),
    (45.0901,"International Relations and Affairs"),
    (45.0902,"National Security Policy Studies"),
    (45.0999,"International Relations and National Security Studies, Other"),
    (45.1001,"Political Science and Government, General"),
    (45.1002,"American Government and Politics (United States"),
    (45.1004,"Political Economy"),
    (45.1099,"Political Science and Government, Other"),
    (45.1101,"Sociology"),
    (45.1201,"Urban Studies/Affairs"),
    (45.1301,"Sociology and Anthropology"),
    (45.1401,"Rural Sociology"),
    (45.9999,"Social Sciences, Other"),
    (46.0000,"Construction Trades, General"),
    (46.0101,"Mason/Masonry"),
    (46.0201,"Carpentry/Carpenter"),
    (46.0301,"Electrical and Power Transmission Installation/Installer, General"),
    (46.0302,"Electrician"),
    (46.0303,"Lineworker"),
    (46.0399,"Electrical and Power Transmission Installers, Other"),
    (46.0401,"Building/Property Maintenance"),
    (46.0402,"Concrete Finishing/Concrete Finisher"),
    (46.0403,"Building/Home/Construction Inspection/Inspector"),
    (46.0404,"Drywall Installation/Drywaller"),
    (46.0406,"Glazier"),
    (46.0408,"Painting/Painter and Wall Coverer"),
    (46.0410,"Roofer"),
    (46.0411,"Metal Building Assembly/Assembler"),
    (46.0412,"Building/Construction Site Management/Manager"),
    (46.0413,"Carpet, Floor, and Tile Worker"),
    (46.0414,"Insulator"),
    (46.0415,"Building Construction Technology"),
    (46.0499,"Building/Construction Finishing, Management, and Inspection, Other"),
    (46.0502,"Pipefitting/Pipefitter and Sprinkler Fitter"),
    (46.0503,"Plumbing Technology/Plumber"),
    (46.0504,"Well Drilling/Driller"),
    (46.0505,"Blasting/Blaster"),
    (46.0599,"Plumbing and Related Water Supply Services, Other"),
    (46.9999,"Construction Trades, Other"),
    (47.0000,"Mechanics and Repairers, General"),
    (47.0101,"Electrical/Electronics Equipment Installation and Repair, General"),
    (47.0102,"Business Machine Repair"),
    (47.0103,"Communications Systems Installation and Repair Technology"),
    (47.0104,"Computer Installation and Repair Technology/Technician"),
    (47.0105,"Industrial Electronics Technology/Technician"),
    (47.0106,"Appliance Installation and Repair Technology/Technician"),
    (47.0110,"Security System Installation, Repair, and Inspection Technology/Technician"),
    (47.0199,"Electrical/Electronics Maintenance and Repair Technology, Other"),
    (47.0201,"Heating, Air Conditioning, Ventilation and Refrigeration Maintenance Technology/"),
    (47.0302,"Heavy Equipment Maintenance Technology/Technician"),
    (47.0303,"Industrial Mechanics and Maintenance Technology"),
    (47.0399,"Heavy/Industrial Equipment Maintenance Technologies, Other"),
    (47.0402,"Gunsmithing/Gunsmith"),
    (47.0403,"Locksmithing and Safe Repair"),
    (47.0404,"Musical Instrument Fabrication and Repair"),
    (47.0408,"Watchmaking and Jewelrymaking"),
    (47.0409,"Parts and Warehousing Operations and Maintenance Technology/Technician"),
    (47.0499,"Precision Systems Maintenance and Repair Technologies, Other"),
    (47.0600,"Vehicle Maintenance and Repair Technologies, General"),
    (47.0603,"Autobody/Collision and Repair Technology/Technician"),
    (47.0604,"Automobile/Automotive Mechanics Technology/Technician"),
    (47.0605,"Diesel Mechanics Technology/Technician"),
    (47.0606,"Small Engine Mechanics and Repair Technology/Technician"),
    (47.0607,"Airframe Mechanics and Aircraft Maintenance Technology/Technician"),
    (47.0608,"Aircraft Powerplant Technology/Technician"),
    (47.0609,"Avionics Maintenance Technology/Technician"),
    (47.0611,"Motorcycle Maintenance and Repair Technology/Technician"),
    (47.0612,"Vehicle Emissions Inspection and Maintenance Technology/Technician"),
    (47.0613,"Medium/Heavy Vehicle and Truck Technology/Technician"),
    (47.0614,"Alternative Fuel Vehicle Technology/Technician"),
    (47.0615,"Engine Machinist"),
    (47.0616,"Marine Maintenance/Fitter and Ship Repair Technology/Technician"),
    (47.0617,"High Performance and Custom Engine Technician/Mechanic"),
    (47.0699,"Vehicle Maintenance and Repair Technologies, Other"),
    (47.9999,"Mechanic and Repair Technologies/Technicians, Other"),
    (48.0000,"Precision Production Trades, General"),
    (48.0303,"Upholstery/Upholsterer"),
    (48.0304,"Shoe, Boot and Leather Repair"),
    (48.0501,"Machine Tool Technology/Machinist"),
    (48.0503,"Machine Shop Technology/Assistant"),
    (48.0506,"Sheet Metal Technology/Sheetworking"),
    (48.0507,"Tool and Die Technology/Technician"),
    (48.0508,"Welding Technology/Welder"),
    (48.0509,"Ironworking/Ironworker"),
    (48.0510,"Computer Numerically Controlled (CNC"),
    (48.0511,"Metal Fabricator"),
    (48.0599,"Precision Metal Working, Other"),
    (48.0701,"Woodworking, General"),
    (48.0702,"Furniture Design and Manufacturing"),
    (48.0703,"Cabinetmaking and Millwork"),
    (48.0799,"Woodworking, Other"),
    (48.0801,"Boilermaking/Boilermaker"),
    (48.9999,"Precision Production, Other"),
    (49.0101,"Aeronautics/Aviation/Aerospace Science and Technology, General"),
    (49.0102,"Airline/Commercial/Professional Pilot and Flight Crew"),
    (49.0104,"Aviation/Airway Management and Operations"),
    (49.0105,"Air Traffic Controller"),
    (49.0106,"Airline Flight Attendant"),
    (49.0108,"Flight Instructor"),
    (49.0199,"Air Transportation, Other"),
    (49.0202,"Construction/Heavy Equipment/Earthmoving Equipment Operation"),
    (49.0205,"Truck and Bus Driver/Commercial Vehicle Operator and Instructor"),
    (49.0206,"Mobil Crane Operation/Operator"),
    (49.0207,"Flagging and Traffic Control"),
    (49.0208,"Railroad and Railway Transportation"),
    (49.0299,"Ground Transportation, Other"),
    (49.0304,"Diver, Professional and Instructor"),
    (49.0309,"Marine Science/Merchant Marine Officer"),
    (49.0399,"Marine Transportation, Other"),
    (49.9999,"Transportation and Materials Moving, Other"),
    (50.0101,"Visual and Performing Arts, General"),
    (50.0102,"Digital Arts"),
    (50.0201,"Crafts/Craft Design, Folk Art and Artisanry"),
    (50.0301,"Dance, General"),
    (50.0302,"Ballet"),
    (50.0399,"Dance, Other"),
    (50.0401,"Design and Visual Communications, General"),
    (50.0402,"Commercial and Advertising Art"),
    (50.0404,"Industrial and Product Design"),
    (50.0406,"Commercial Photography"),
    (50.0407,"Fashion/Apparel Design"),
    (50.0408,"Interior Design"),
    (50.0409,"Graphic Design"),
    (50.0410,"Illustration"),
    (50.0411,"Game and Interactive Media Design"),
    (50.0499,"Design and Applied Arts, Other"),
    (50.0501,"Drama and Dramatics/Theatre Arts, General"),
    (50.0502,"Technical Theatre/Theatre Design and Technology"),
    (50.0504,"Playwriting and Screenwriting"),
    (50.0505,"Theatre Literature, History and Criticism"),
    (50.0506,"Acting"),
    (50.0507,"Directing and Theatrical Production"),
    (50.0509,"Musical Theatre"),
    (50.0510,"Costume Design"),
    (50.0599,"Dramatic/Theatre Arts and Stagecraft, Other"),
    (50.0601,"Film/Cinema/Video Studies"),
    (50.0602,"Cinematography and Film/Video Production"),
    (50.0605,"Photography"),
    (50.0607,"Documentary Production"),
    (50.0699,"Film/Video and Photographic Arts, Other"),
    (50.0701,"Art/Art Studies, General"),
    (50.0702,"Fine/Studio Arts, General"),
    (50.0703,"Art History, Criticism and Conservation"),
    (50.0705,"Drawing"),
    (50.0706,"Intermedia/Multimedia"),
    (50.0708,"Painting"),
    (50.0709,"Sculpture"),
    (50.0710,"Printmaking"),
    (50.0711,"Ceramic Arts and Ceramics"),
    (50.0712,"Fiber, Textile and Weaving Arts"),
    (50.0713,"Metal and Jewelry Arts"),
    (50.0799,"Fine Arts and Art Studies, Other"),
    (50.0901,"Music, General"),
    (50.0902,"Music History, Literature, and Theory"),
    (50.0903,"Music Performance, General"),
    (50.0904,"Music Theory and Composition"),
    (50.0905,"Musicology and Ethnomusicology"),
    (50.0906,"Conducting"),
    (50.0907,"Keyboard Instruments"),
    (50.0908,"Voice and Opera"),
    (50.0910,"Jazz/Jazz Studies"),
    (50.0911,"Stringed Instruments"),
    (50.0912,"Music Pedagogy"),
    (50.0913,"Music Technology"),
    (50.0914,"Brass Instruments"),
    (50.0915,"Woodwind Instruments"),
    (50.0916,"Percussion Instruments"),
    (50.0999,"Music, Other"),
    (50.1001,"Arts, Entertainment,and Media Management, General"),
    (50.1002,"Fine and Studio Arts Management"),
    (50.1003,"Music Management"),
    (50.1004,"Theatre/Theatre Arts Management"),
    (50.1099,"Arts, Entertainment, and Media Management, Other"),
    (50.9999,"Visual and Performing Arts, Other"),
    (51.0000,"Health Services/Allied Health/Health Sciences, General"),
    (51.0001,"Health and Wellness, General"),
    (51.0101,"Chiropractic"),
    (51.0201,"Communication Sciences and Disorders, General"),
    (51.0202,"Audiology/Audiologist"),
    (51.0203,"Speech-Language Pathology/Pathologist"),
    (51.0204,"Audiology/Audiologist and Speech-Language Pathology/Pathologist"),
    (51.0299,"Communication Disorders Sciences and Services, Other"),
    (51.0401,"Dentistry"),
    (51.0501,"Dental Clinical Sciences, General"),
    (51.0502,"Advanced General Dentistry"),
    (51.0503,"Oral Biology and Oral and Maxillofacial Pathology"),
    (51.0504,"Dental Public Health and Education"),
    (51.0505,"Dental Materials"),
    (51.0506,"Endodontics/Endodontology"),
    (51.0507,"Oral/Maxillofacial Surgery"),
    (51.0508,"Orthodontics/Orthodontology"),
    (51.0509,"Pediatric Dentistry/Pedodontics"),
    (51.0510,"Periodontics/Periodontology"),
    (51.0511,"Prosthodontics/Prosthodontology"),
    (51.0599,"Advanced/Graduate Dentistry and Oral Sciences, Other"),
    (51.0601,"Dental Assisting/Assistant"),
    (51.0602,"Dental Hygiene/Hygienist"),
    (51.0603,"Dental Laboratory Technology/Technician"),
    (51.0699,"Dental Services and Allied Professions, Other"),
    (51.0701,"Health/Health Care Administration/Management"),
    (51.0702,"Hospital and Health Care Facilities Administration/Management"),
    (51.0703,"Health Unit Coordinator/Ward Clerk"),
    (51.0704,"Health Unit Manager/Ward Supervisor"),
    (51.0705,"Medical Office Management/Administration"),
    (51.0706,"Health Information/Medical Records Administration/Administrator"),
    (51.0707,"Health Information/Medical Records Technology/Technician"),
    (51.0708,"Medical Transcription/Transcriptionist"),
    (51.0709,"Medical Office Computer Specialist/Assistant"),
    (51.0710,"Medical Office Assistant/Specialist"),
    (51.0711,"Medical/Health Management and Clinical Assistant/Specialist"),
    (51.0712,"Medical Reception/Receptionist"),
    (51.0713,"Medical Insurance Coding Specialist/Coder"),
    (51.0714,"Medical Insurance Specialist/Medical Biller"),
    (51.0715,"Health/Medical Claims Examiner"),
    (51.0716,"Medical Administrative/Executive Assistant and Medical Secretary"),
    (51.0717,"Medical Staff Services Technology/Technician"),
    (51.0718,"Long Term Care Administration/Management"),
    (51.0719,"Clinical Research Coordinator"),
    (51.0799,"Health and Medical Administrative Services, Other"),
    (51.0801,"Medical/Clinical Assistant"),
    (51.0802,"Clinical/Medical Laboratory Assistant"),
    (51.0803,"Occupational Therapist Assistant"),
    (51.0805,"Pharmacy Technician/Assistant"),
    (51.0806,"Physical Therapy Technician/Assistant"),
    (51.0808,"Veterinary/Animal Health Technology/Technician and Veterinary Assistant"),
    (51.0809,"Anesthesiologist Assistant"),
    (51.0810,"Emergency Care Attendant (EMT Ambulance)"),
    (51.0811,"Pathology/Pathologist Assistant"),
    (51.0812,"Respiratory Therapy Technician/Assistant"),
    (51.0813,"Chiropractic Assistant/Technician"),
    (51.0814,"Radiologist Assistant"),
    (51.0815,"Lactation Consultant"),
    (51.0816,"Speech-Language Pathology Assistant"),
    (51.0899,"Allied Health and Medical Assisting Services, Other"),
    (51.0901,"Cardiovascular Technology/Technologist"),
    (51.0902,"Electrocardiograph Technology/Technician"),
    (51.0903,"Electroneurodiagnostic/Electroencephalographic Technology/Technologist"),
    (51.0904,"Emergency Medical Technology/Technician (EMT Paramedic)"),
    (51.0905,"Nuclear Medical Technology/Technologist"),
    (51.0906,"Perfusion Technology/Perfusionist"),
    (51.0907,"Medical Radiologic Technology/Science - Radiation Therapist"),
    (51.0908,"Respiratory Care Therapy/Therapist"),
    (51.0909,"Surgical Technology/Technologist"),
    (51.0910,"Diagnostic Medical Sonography/Sonographer and Ultrasound Technician"),
    (51.0911,"Radiologic Technology/Science - Radiographer"),
    (51.0912,"Physician Assistant"),
    (51.0913,"Athletic Training/Trainer"),
    (51.0914,"Gene/Genetic Therapy"),
    (51.0915,"Cardiopulmonary Technology/Technologist"),
    (51.0916,"Radiation Protection/Health Physics Technician"),
    (51.0917,"Polysomnography"),
    (51.0918,"Hearing Instrument Specialist"),
    (51.0919,"Mammography Technician/Technology"),
    (51.0920,"Magnetic Resonance Imaging (MRI"),
    (51.0999,"Allied Health Diagnostic, Intervention, and Treatment Professions, Other"),
    (51.1001,"Blood Bank Technology Specialist"),
    (51.1002,"Cytotechnology/Cytotechnologist"),
    (51.1003,"Hematology Technology/Technician"),
    (51.1004,"Clinical/Medical Laboratory Technician"),
    (51.1005,"Clinical Laboratory Science/Medical Technology/Technologist"),
    (51.1006,"Ophthalmic Laboratory Technology/Technician"),
    (51.1007,"Histologic Technology/Histotechnologist"),
    (51.1008,"Histologic Technician"),
    (51.1009,"Phlebotomy Technician/Phlebotomist"),
    (51.1010,"Cytogenetics/Genetics/Clinical Genetics Technology/Technologist"),
    (51.1011,"Renal/Dialysis Technologist/Technician"),
    (51.1012,"Sterile Processing Technology/Technician"),
    (51.1099,"Clinical/Medical Laboratory Science and Allied Professions, Other"),
    (51.1101,"Pre-Dentistry Studies"),
    (51.1102,"Pre-Medicine/Pre-Medical Studies"),
    (51.1103,"Pre-Pharmacy Studies"),
    (51.1104,"Pre-Veterinary Studies"),
    (51.1105,"Pre-Nursing Studies"),
    (51.1106,"Pre-Chiropractic Studies"),
    (51.1107,"Pre-Occupational Therapy Studies"),
    (51.1108,"Pre-Optometry Studies"),
    (51.1109,"Pre-Physical Therapy Studies"),
    (51.1199,"Health/Medical Preparatory Programs, Other"),
    (51.1201,"Medicine"),
    (51.1401,"Medical Scientist"),
    (51.1501,"Substance Abuse/Addiction Counseling"),
    (51.1502,"Psychiatric/Mental Health Services Technician"),
    (51.1503,"Clinical/Medical Social Work"),
    (51.1504,"Community Health Services/Liaison/Counseling"),
    (51.1505,"Marriage and Family Therapy/Counseling"),
    (51.1506,"Clinical Pastoral Counseling/Patient Counseling"),
    (51.1507,"Psychoanalysis and Psychotherapy"),
    (51.1508,"Mental Health Counseling/Counselor"),
    (51.1509,"Genetic Counseling/Counselor"),
    (51.1599,"Mental and Social Health Services and Allied Professions, Other"),
    (51.1701,"Optometry"),
    (51.1801,"Opticianry/Ophthalmic Dispensing Optician"),
    (51.1802,"Optometric Technician/Assistant"),
    (51.1803,"Ophthalmic Technician/Technologist"),
    (51.1804,"Orthoptics/Orthoptist"),
    (51.1899,"Ophthalmic and Optometric Support Services and Allied Professions, Other"),
    (51.1901,"Osteopathic Medicine/Osteopathy"),
    (51.2001,"Pharmacy"),
    (51.2002,"Pharmacy Administration and Pharmacy Policy and Regulatory Affairs"),
    (51.2003,"Pharmaceutics and Drug Design"),
    (51.2004,"Medicinal and Pharmaceutical Chemistry"),
    (51.2005,"Natural Products Chemistry and Pharmacognosy"),
    (51.2006,"Clinical and Industrial Drug Development"),
    (51.2007,"Pharmacoeconomics/Pharmaceutical Economics"),
    (51.2008,"Clinical, Hospital, and Managed Care Pharmacy"),
    (51.2009,"Industrial and Physical Pharmacy and Cosmetic Sciences"),
    (51.2010,"Pharmaceutical Sciences"),
    (51.2011,"Pharmaceutical Marketing and Management"),
    (51.2099,"Pharmacy, Pharmaceutical Sciences, and Administration, Other"),
    (51.2101,"Podiatric Medicine/Podiatry"),
    (51.2201,"Public Health, General"),
    (51.2202,"Environmental Health"),
    (51.2205,"Health/Medical Physics"),
    (51.2206,"Occupational Health and Industrial Hygiene"),
    (51.2207,"Public Health Education and Promotion"),
    (51.2208,"Community Health and Preventive Medicine"),
    (51.2209,"Maternal and Child Health"),
    (51.2210,"International Public Health/International Health"),
    (51.2211,"Health Services Administration"),
    (51.2212,"Behavioral Aspects of Health"),
    (51.2299,"Public Health, Other"),
    (51.2301,"Art Therapy/Therapist"),
    (51.2302,"Dance Therapy/Therapist"),
    (51.2305,"Music Therapy/Therapist"),
    (51.2306,"Occupational Therapy/Therapist"),
    (51.2307,"Orthotist/Prosthetist"),
    (51.2308,"Physical Therapy/Therapist"),
    (51.2309,"Therapeutic Recreation/Recreational Therapy"),
    (51.2310,"Vocational Rehabilitation Counseling/Counselor"),
    (51.2311,"Kinesiotherapy/Kinesiotherapist"),
    (51.2312,"Assistive/Augmentative Technology and Rehabilitation Engineering"),
    (51.2313,"Animal-Assisted Therapy"),
    (51.2314,"Rehabilitation Science"),
    (51.2399,"Rehabilitation and Therapeutic Professions, Other"),
    (51.2401,"Veterinary Medicine"),
    (51.2501,"Veterinary Sciences/Veterinary Clinical Sciences, General"),
    (51.2503,"Veterinary Physiology"),
    (51.2504,"Veterinary Microbiology and Immunobiology"),
    (51.2505,"Veterinary Pathology and Pathobiology"),
    (51.2507,"Large Animal/Food Animal and Equine Surgery and Medicine"),
    (51.2508,"Small/Companion Animal Surgery and Medicine"),
    (51.2509,"Comparative and Laboratory Animal Medicine"),
    (51.2510,"Veterinary Preventive Medicine, Epidemiology, and Public Health"),
    (51.2511,"Veterinary Infectious Diseases"),
    (51.2599,"Veterinary Biomedical and Clinical Sciences, Other"),
    (51.2601,"Health Aide"),
    (51.2602,"Home Health Aide/Home Attendant"),
    (51.2603,"Medication Aide"),
    (51.2604,"Rehabilitation Aide"),
    (51.2699,"Health Aides/Attendants/Orderlies, Other"),
    (51.2703,"Medical Illustration/Medical Illustrator"),
    (51.2706,"Medical Informatics"),
    (51.2799,"Medical Illustration and Informatics, Other"),
    (51.3101,"Dietetics/Dietitian"),
    (51.3102,"Clinical Nutrition/Nutritionist"),
    (51.3103,"Dietetic Technician"),
    (51.3104,"Dietitian Assistant"),
    (51.3199,"Dietetics and Clinical Nutrition Services, Other"),
    (51.3201,"Bioethics/Medical Ethics"),
    (51.3300,"Alternative and Complementary Medicine and Medical Systems, General"),
    (51.3301,"Acupuncture and Oriental Medicine"),
    (51.3302,"Traditional Chinese Medicine and Chinese Herbology"),
    (51.3303,"Naturopathic Medicine/Naturopathy"),
    (51.3304,"Homeopathic Medicine/Homeopathy"),
    (51.3305,"Ayurvedic Medicine/Ayurveda"),
    (51.3306,"Holistic Health"),
    (51.3399,"Alternative and Complementary Medicine and Medical Systems, Other"),
    (51.3401,"Direct Entry Midwifery"),
    (51.3499,"Alternative and Complementary Medical Support Services, Other"),
    (51.3501,"Massage Therapy/Therapeutic Massage"),
    (51.3502,"Asian Bodywork Therapy"),
    (51.3503,"Somatic Bodywork"),
    (51.3599,"Somatic Bodywork and Related Therapeutic Services, Other"),
    (51.3601,"Movement Therapy and Movement Education"),
    (51.3602,"Yoga Teacher Training/Yoga Therapy"),
    (51.3603,"Hypnotherapy/Hypnotherapist"),
    (51.3699,"Movement and Mind-Body Therapies and Education, Other"),
    (51.3701,"Aromatherapy"),
    (51.3702,"Herbalism/Herbalist"),
    (51.3703,"Polarity Therapy"),
    (51.3704,"Reiki"),
    (51.3799,"Energy and Biologically Based Therapies, Other"),
    (51.3801,"Registered Nursing/Registered Nurse"),
    (51.3802,"Nursing Administration"),
    (51.3803,"Adult Health Nurse/Nursing"),
    (51.3804,"Nurse Anesthetist"),
    (51.3805,"Family Practice Nurse/Nursing"),
    (51.3806,"Maternal/Child Health and Neonatal Nurse/Nursing"),
    (51.3807,"Nurse Midwife/Nursing Midwifery"),
    (51.3808,"Nursing Science"),
    (51.3809,"Pediatric Nurse/Nursing"),
    (51.3810,"Psychiatric/Mental Health Nurse/Nursing"),
    (51.3811,"Public Health/Community Nurse/Nursing"),
    (51.3812,"Perioperative/Operating Room and Surgical Nurse/Nursing"),
    (51.3813,"Clinical Nurse Specialist"),
    (51.3814,"Critical Care Nursing"),
    (51.3815,"Occupational and Environmental Health Nursing"),
    (51.3816,"Emergency Room/Trauma Nursing"),
    (51.3817,"Nursing Education"),
    (51.3818,"Nursing Practice"),
    (51.3819,"Palliative Care Nursing"),
    (51.3820,"Clinical Nurse Leader"),
    (51.3821,"Geriatric Nurse/Nursing"),
    (51.3822,"Women's Health Nurse/Nursing"),
    (51.3899,"Registered Nursing, Nursing Administration, Nursing Research and Clinical Nursin"),
    (51.3901,"Licensed Practical/Vocational Nurse Training"),
    (51.3902,"Nursing Assistant/Aide and Patient Care Assistant/Aide"),
    (51.3999,"Practical Nursing, Vocational Nursing and Nursing Assistants, Other"),
    (51.9999,"Health Professions and Related Clinical Sciences, Other"),
    (52.0101,"Business/Commerce, General"),
    (52.0201,"Business Administration and Management, General"),
    (52.0202,"Purchasing, Procurement/Acquisitions and Contracts Management"),
    (52.0203,"Logistics, Materials, and Supply Chain Management"),
    (52.0204,"Office Management and Supervision"),
    (52.0205,"Operations Management and Supervision"),
    (52.0206,"Non-Profit/Public/Organizational Management"),
    (52.0207,"Customer Service Management"),
    (52.0208,"E-Commerce/Electronic Commerce"),
    (52.0209,"Transportation/Mobility Management"),
    (52.0210,"Research and Development Management"),
    (52.0211,"Project Management"),
    (52.0212,"Retail Management"),
    (52.0213,"Organizational Leadership"),
    (52.0299,"Business Administration, Management and Operations, Other"),
    (52.0301,"Accounting"),
    (52.0302,"Accounting Technology/Technician and Bookkeeping"),
    (52.0303,"Auditing"),
    (52.0304,"Accounting and Finance"),
    (52.0305,"Accounting and Business/Management"),
    (52.0399,"Accounting and Related Services, Other"),
    (52.0401,"Administrative Assistant and Secretarial Science, General"),
    (52.0402,"Executive Assistant/Executive Secretary"),
    (52.0406,"Receptionist"),
    (52.0407,"Business/Office Automation/Technology/Data Entry"),
    (52.0408,"General Office Occupations and Clerical Services"),
    (52.0409,"Parts, Warehousing, and Inventory Management Operations"),
    (52.0410,"Traffic, Customs, and Transportation Clerk/Technician"),
    (52.0411,"Customer Service Support/Call Center/Teleservice Operation"),
    (52.0499,"Business Operations Support and Secretarial Services, Other"),
    (52.0501,"Business/Corporate Communications"),
    (52.0601,"Business/Managerial Economics"),
    (52.0701,"Entrepreneurship/Entrepreneurial Studies"),
    (52.0702,"Franchising and Franchise Operations"),
    (52.0703,"Small Business Administration/Management"),
    (52.0799,"Entrepreneurial and Small Business Operations, Other"),
    (52.0801,"Finance, General"),
    (52.0803,"Banking and Financial Support Services"),
    (52.0804,"Financial Planning and Services"),
    (52.0806,"International Finance"),
    (52.0807,"Investments and Securities"),
    (52.0808,"Public Finance"),
    (52.0809,"Credit Management"),
    (52.0899,"Finance and Financial Management Services, Other"),
    (52.0901,"Hospitality Administration/Management, General"),
    (52.0903,"Tourism and Travel Services Management"),
    (52.0904,"Hotel/Motel Administration/Management"),
    (52.0905,"Restaurant/Food Services Management"),
    (52.0906,"Resort Management"),
    (52.0907,"Meeting and Event Planning"),
    (52.0908,"Casino Management"),
    (52.0909,"Hotel, Motel, and Restaurant Management"),
    (52.0999,"Hospitality Administration/Management, Other"),
    (52.1001,"Human Resources Management/Personnel Administration, General"),
    (52.1002,"Labor and Industrial Relations"),
    (52.1003,"Organizational Behavior Studies"),
    (52.1004,"Labor Studies"),
    (52.1005,"Human Resources Development"),
    (52.1099,"Human Resources Management and Services, Other"),
    (52.1101,"International Business/Trade/Commerce"),
    (52.1201,"Management Information Systems, General"),
    (52.1206,"Information Resources Management"),
    (52.1207,"Knowledge Management"),
    (52.1299,"Management Information Systems and Services, Other"),
    (52.1301,"Management Science"),
    (52.1302,"Business Statistics"),
    (52.1304,"Actuarial Science"),
    (52.1399,"Management Sciences and Quantitative Methods, Other"),
    (52.1401,"Marketing/Marketing Management, General"),
    (52.1402,"Marketing Research"),
    (52.1403,"International Marketing"),
    (52.1499,"Marketing, Other"),
    (52.1501,"Real Estate"),
    (52.1601,"Taxation"),
    (52.1701,"Insurance"),
    (52.1801,"Sales, Distribution, and Marketing Operations, General"),
    (52.1802,"Merchandising and Buying Operations"),
    (52.1803,"Retailing and Retail Operations"),
    (52.1804,"Selling Skills and Sales Operations"),
    (52.1899,"General Merchandising, Sales, and Related Marketing Operations, Other"),
    (52.1901,"Auctioneering"),
    (52.1902,"Fashion Merchandising"),
    (52.1903,"Fashion Modeling"),
    (52.1904,"Apparel and Accessories Marketing Operations"),
    (52.1905,"Tourism and Travel Services Marketing Operations"),
    (52.1906,"Tourism Promotion Operations"),
    (52.1907,"Vehicle and Vehicle Parts and Accessories Marketing Operations"),
    (52.1908,"Business and Personal/Financial Services Marketing Operations"),
    (52.1909,"Special Products Marketing Operations"),
    (52.1910,"Hospitality and Recreation Marketing Operations"),
    (52.1999,"Specialized Merchandising, Sales, and Marketing Operations, Other"),
    (52.2001,"Construction Management"),
    (52.2101,"Telecommunications Management"),
    (52.9999,"Business, Management, Marketing, and Related Support Services, Other"),
    (54.0101,"History, General"),
    (54.0102,"American History (United States)"),
    (54.0103,"European History"),
    (54.0104,"History and Philosophy of Science and Technology"),
    (54.0105,"Public/Applied History"),
    (54.0106,"Asian History"),
    (54.0108,"Military History"),
    (54.0199,"History, Other")
)

AWARD_LEVEL_CHOICES = (
    (1,"Award of less than 1 academic year"),
    (2,"Award of at least 1 but less than 2 academic years"),
    (3,"Associate's degree"),
    (4,"Award of at least 2 but less than 4 academic years"),
    (5,"Bachelor's degree"),
    (6,"Postbaccalaureate certificate"),
    (7,"Master's degree"),
    (8,"Post-master's certificate"),
    (9,"Doctor's degree"),
    (10,"Postbaccalaureate or Post-master's certificate"),
    (17,"Doctor's degree - research/scholarship"),
    (18,"Doctor's degree - professional practice"),
    (19,"Doctor's degree - other"),
)

EFA_LEVEL_CHOICES = (
    (11,"All students, Undergraduate, Non-degree/certificate-seeking"),
    (12,"All students, Graduate"),
    (21,"Full-time students total"),
    (22,"Full-time students, Undergraduate total"),
    (23,"Full-time students, Undergraduate, Degree/certificate-seeking total"),
    (24,"Full-time students, Undergraduate, Degree/certificate-seeking, First-time"),
    (25,"Full-time students, Undergraduate, Degree/certificate-seeking, Other degree/certificate-seeking"),
    (39,"Full-time students, Undergraduate, Other degree/certifcate-seeking, Transfer-ins"),
    (40,"Full-time students, Undergraduate, Other degree/certifcate-seeking, Continuing"),
    (31,"Full-time students, Undergraduate, Non-degree/certificate-seeking"),
    (32,"Full-time students, Graduate"),
    (41,"Part-time students total"),
    (42,"Part-time students, Undergraduate total"),
    (43,"Part-time students, Undergraduate, Degree/certificate-seeking total"),
    (44,"Part-time students, Undergraduate, Degree/certificate-seeking, First-time"),
    (45,"Part-time students, Undergraduate, Degree/certificate-seeking, Other degree/certificate-seeking"),
    (59,"Part-time students, Undergraduate, Other degree/certifcate-seeking, Transfer-ins"),
    (60,"Part-time students, Undergraduate, Other degree/certifcate-seeking, Continuing"),
    (51,"Part-time students, Undergraduate, Non-degree/certificate-seeking"),
    (52,"Part-time students, Graduate"),
)

SECTION_CHOICES = (
    (1, "Full-time"),
    (2,"Part-time"),
    (3,"All students"),
)

LSTUDY_A_CHOICES = (
    (1,"Undergraduate"),
    (3,"Graduate"),
    (4,"All students"),
)

LSTUDY_B_CHOICES = (
    (1,"All Students total"),
    (2,"Undergraduate"),
    (5,"Graduate"),
)

EFC_STATE_CHOICES = (
    (99,"All first-time degree/certificate seeking undergraduates, total"),
    (58,"US total"),
    (1,"Alabama"),
    (2,"Alaska"),
    (4,"Arizona"),
    (5,"Arkansas"),
    (6,"California"),
    (8,"Colorado"),
    (9,"Connecticut"),
    (10,"Delaware"),
    (11,"District of Columbia"),
    (12,"Florida"),
    (13,"Georgia"),
    (15,"Hawaii"),
    (16,"Idaho"),
    (17,"Illinois"),
    (18,"Indiana"),
    (19,"Iowa"),
    (20,"Kansas"),
    (21,"Kentucky"),
    (22,"Louisiana"),
    (23,"Maine"),
    (24,"Maryland"),
    (25,"Massachusetts"),
    (26,"Michigan"),
    (27,"Minnesota"),
    (28,"Mississippi"),
    (29,"Missouri"),
    (30,"Montana"),
    (31,"Nebraska"),
    (32,"Nevada"),
    (33,"New Hampshire"),
    (34,"New Jersey"),
    (35,"New Mexico"),
    (36,"New York"),
    (37,"North Carolina"),
    (38,"North Dakota"),
    (39,"Ohio"),
    (40,"Oklahoma"),
    (41,"Oregon"),
    (42,"Pennsylvania"),
    (44,"Rhode Island"),
    (45,"South Carolina"),
    (46,"South Dakota"),
    (47,"Tennessee"),
    (48,"Texas"),
    (49,"Utah"),
    (50,"Vermont"),
    (51,"Virginia"),
    (53,"Washington"),
    (54,"West Virginia"),
    (55,"Wisconsin"),
    (56,"Wyoming"),
    (57,"State unknown"),
    (89,"Outlying areas total"),
    (60,"American Samoa"),
    (64,"Federated States of Micronesia"),
    (66,"Guam"),
    (68,"Marshall Islands"),
    (69,"Northern Marianas"),
    (70,"Palau"),
    (72,"Puerto Rico"),
    (78,"Virgin Islands"),
    (90,"Foreign countries"),
    (98,"Residence not reported"),
)

STATE_ABBR = (
    ("AL","Alabama"),
    ("AK","Alaska"),
    ("AS","American Samoa"),
    ("AZ","Arizona"),
    ("AR","Arkansas"),
    ("CA","California"),
    ("CO","Colorado"),
    ("CT","Connecticut"),
    ("DE","Delaware"),
    ("DC","District of Columbia"),
    ("FM","Federated States of Micronesia"),
    ("FL","Florida"),
    ("GA","Georgia"),
    ("GU","Guam"),
    ("HI","Hawaii"),
    ("ID","Idaho"),
    ("IL","Illinois"),
    ("IN","Indiana"),
    ("IA","Iowa"),
    ("KS","Kansas"),
    ("KY","Kentucky"),
    ("LA","Louisiana"),
    ("ME","Maine"),
    ("MH","Marshall Islands"),
    ("MD","Maryland"),
    ("MA","Massachusetts"),
    ("MI","Michigan"),
    ("MN","Minnesota"),
    ("MS","Mississippi"),
    ("MO","Missouri"),
    ("MT","Montana"),
    ("NE","Nebraska"),
    ("NV","Nevada"),
    ("NH","New Hampshire"),
    ("NJ","New Jersey"),
    ("NM","New Mexico"),
    ("NY","New York"),
    ("NC","North Carolina"),
    ("ND","North Dakota"),
    ("MP","Northern Mariana Islands"),
    ("OH","Ohio"),
    ("OK","Oklahoma"),
    ("OR","Oregon"),
    ("PW","Palau"),
    ("PA","Pennsylvania"),
    ("PR","Puerto Rico"),
    ("RI","Rhode Island"),
    ("SC","South Carolina"),
    ("SD","South Dakota"),
    ("TN","Tennessee"),
    ("TX","Texas"),
    ("UT","Utah"),
    ("VT","Vermont"),
    ("VI","Virgin Islands"),
    ("VA","Virginia"),
    ("WA","Washington"),
    ("WV","West Virginia"),
    ("WI","Wisconsin"),
    ("WY","Wyoming"),
)

class DegreesbyMajorEthnicity(models.Model):
    # Number of students receiving degrees by type of program, award level,
    # first/second major, ethnicity, and gender.
    unitid = models.ForeignKey('UnivBaseTable',db_column='UNITID',related_name='awardsdetails') 
    cipcode = models.FloatField(db_column='CIPCODE', verbose_name="cipcode", choices=CIPCODE_CHOICES)
    majornum = models.IntegerField(db_column='MAJORNUM', verbose_name="first or second major")
    awlevel = models.IntegerField(db_column='AWLEVEL', verbose_name="award level code", choices=AWARD_LEVEL_CHOICES)
    xcgrand_tot = models.CharField(db_column='XCTOTALT', max_length=1) 
    total_degrees = models.IntegerField(db_column='CTOTALT', verbose_name="grand total")
    xctot_male = models.CharField(db_column='XCTOTALM', max_length=1) 
    total_male_degrees = models.IntegerField(db_column='CTOTALM', verbose_name="grand total men")
    xctot_female = models.CharField(db_column='XCTOTALW', max_length=1) 
    total_female_degrees = models.IntegerField(db_column='CTOTALW', verbose_name="grand total women")
    xctot_aian = models.CharField(db_column='XCAIANT', max_length=1) 
    c_tot_aian = models.IntegerField(db_column='CAIANT', verbose_name="american indian or alaska native total")
    xcaian_male = models.CharField(db_column='XCAIANM', max_length=1) 
    c_aian_male = models.IntegerField(db_column='CAIANM', verbose_name="american indian or alaska native men")
    xcaian_female = models.CharField(db_column='XCAIANW', max_length=1) 
    c_aian_female = models.IntegerField(db_column='CAIANW', verbose_name="american indian or alaska native women")
    xctot_asian = models.CharField(db_column='XCASIAT', max_length=1) 
    c_tot_asian = models.IntegerField(db_column='CASIAT', verbose_name="asian total")
    xcasian_male = models.CharField(db_column='XCASIAM', max_length=1) 
    c_asian_male = models.IntegerField(db_column='CASIAM', verbose_name="asian men")
    xcasian_female = models.CharField(db_column='XCASIAW', max_length=1) 
    c_asian_female = models.IntegerField(db_column='CASIAW', verbose_name="asian women")
    xctot_black = models.CharField(db_column='XCBKAAT', max_length=1) 
    c_tot_black = models.IntegerField(db_column='CBKAAT', verbose_name="black or african american total")
    xcblack_male = models.CharField(db_column='XCBKAAM', max_length=1) 
    c_black_male = models.IntegerField(db_column='CBKAAM', verbose_name="black or african american men")
    xcblack_female = models.CharField(db_column='XCBKAAW', max_length=1) 
    c_black_female = models.IntegerField(db_column='CBKAAW', verbose_name="black or african american women")
    xctot_hispanic = models.CharField(db_column='XCHISPT', max_length=1) 
    c_tot_hispanic = models.IntegerField(db_column='CHISPT', verbose_name="hispanic or latino total")
    xchispanic_male = models.CharField(db_column='XCHISPM', max_length=1) 
    c_hispanic_male = models.IntegerField(db_column='CHISPM', verbose_name="hispanic or latino men")
    xchispanic_female = models.CharField(db_column='XCHISPW', max_length=1) 
    c_hispanic_female = models.IntegerField(db_column='CHISPW', verbose_name="hispanic or latino women")
    xctot_nhpi = models.CharField(db_column='XCNHPIT', max_length=1) 
    c_tot_nhpi = models.IntegerField(db_column='CNHPIT', verbose_name="native hawaiian or other pacific islander total")
    xcnhpi_male = models.CharField(db_column='XCNHPIM', max_length=1) 
    c_nhpi_male = models.IntegerField(db_column='CNHPIM', verbose_name="native hawaiian or other pacific islander men")
    xcnhpi_female = models.CharField(db_column='XCNHPIW', max_length=1) 
    c_nhpi_female = models.IntegerField(db_column='CNHPIW', verbose_name="native hawaiian or other pacific islander women")
    xctot_white = models.CharField(db_column='XCWHITT', max_length=1) 
    c_tot_white = models.IntegerField(db_column='CWHITT', verbose_name="white total")
    xcwhite_male = models.CharField(db_column='XCWHITM', max_length=1) 
    c_white_male = models.IntegerField(db_column='CWHITM', verbose_name="white men")
    xcwhite_female = models.CharField(db_column='XCWHITW', max_length=1) 
    c_white_female = models.IntegerField(db_column='CWHITW', verbose_name="white women")
    xctot_biracial = models.CharField(db_column='XC2MORT', max_length=1) 
    c_tot_biracial = models.IntegerField(db_column='C2MORT', verbose_name="two or more races total")
    xcbiracial_male = models.CharField(db_column='XC2MORM', max_length=1) 
    c_biracial_male = models.IntegerField(db_column='C2MORM', verbose_name="two or more races men")
    xcbiracial_female = models.CharField(db_column='XC2MORW', max_length=1) 
    c_biracial_female = models.IntegerField(db_column='C2MORW', verbose_name="two or more races women")
    xctot_unknown = models.CharField(db_column='XCUNKNT', max_length=1) 
    c_tot_unknown = models.IntegerField(db_column='CUNKNT', verbose_name="race/ethnicity unknown total")
    xcunknown_male = models.CharField(db_column='XCUNKNM', max_length=1) 
    c_unknown_male = models.IntegerField(db_column='CUNKNM', verbose_name="race/ethnicity unknown men")
    xcunknown_female = models.CharField(db_column='XCUNKNW', max_length=1) 
    c_unknown_female = models.IntegerField(db_column='CUNKNW', verbose_name="race/ethnicity unknown women")
    xcnralt = models.CharField(db_column='XCNRALT', max_length=1) 
    cnralt = models.IntegerField(db_column='CNRALT', verbose_name="nonresident alien total")
    xcnralm = models.CharField(db_column='XCNRALM', max_length=1) 
    cnralm = models.IntegerField(db_column='CNRALM', verbose_name="nonresident alien men")
    xcnralw = models.CharField(db_column='XCNRALW', max_length=1) 
    cnralw_field = models.IntegerField(db_column='CNRALW  ') 

    class Meta:
        managed = False
        db_table = 'c2013_a'


class DegreesbyEthnicity(models.Model):
    # Number of students receiving degrees/certificates by ethnicity and gender
    unitid = models.OneToOneField('UnivBaseTable', db_column='UNITID',related_name="demographics") 
    xcsgrand_tot = models.CharField(db_column='XCSTOTLT', max_length=1) 
    cs_grand_tot = models.IntegerField(db_column='CSTOTLT', verbose_name="grand total")
    xcstot_male = models.CharField(db_column='XCSTOTLM', max_length=1) 
    cs_tot_male = models.IntegerField(db_column='CSTOTLM', verbose_name="grand total men")
    xcstot_female = models.CharField(db_column='XCSTOTLW', max_length=1) 
    cs_tot_female = models.IntegerField(db_column='CSTOTLW', verbose_name="grand total women")
    xcstot_aian = models.CharField(db_column='XCSAIANT', max_length=1) 
    cs_tot_aian = models.IntegerField(db_column='CSAIANT', verbose_name="american indian or alaska native total")
    xcsaian_male = models.CharField(db_column='XCSAIANM', max_length=1) 
    cs_aian_male = models.IntegerField(db_column='CSAIANM', verbose_name="american indian or alaska native men")
    xcsaianfemale = models.CharField(db_column='XCSAIANW', max_length=1) 
    cs_aian_female = models.IntegerField(db_column='CSAIANW', verbose_name="american indian or alaska native women")
    xcstot_asian = models.CharField(db_column='XCSASIAT', max_length=1) 
    cs_tot_asian = models.IntegerField(db_column='CSASIAT', verbose_name="asian total")
    xcsasian_male = models.CharField(db_column='XCSASIAM', max_length=1) 
    cs_asian_male = models.IntegerField(db_column='CSASIAM', verbose_name="asian men")
    xcsasian_female = models.CharField(db_column='XCSASIAW', max_length=1) 
    cs_asian_female = models.IntegerField(db_column='CSASIAW', verbose_name="asian women")
    xcstot_black = models.CharField(db_column='XCSBKAAT', max_length=1) 
    cs_tot_black = models.IntegerField(db_column='CSBKAAT', verbose_name="black or african american total")
    xcsblack_male = models.CharField(db_column='XCSBKAAM', max_length=1) 
    cs_black_male = models.IntegerField(db_column='CSBKAAM', verbose_name="black or african american men")
    xcsblack_female = models.CharField(db_column='XCSBKAAW', max_length=1) 
    cs_black_female = models.IntegerField(db_column='CSBKAAW', verbose_name="black or african american women")
    xcstot_hispanic = models.CharField(db_column='XCSHISPT', max_length=1) 
    cs_tot_hispanic = models.IntegerField(db_column='CSHISPT', verbose_name="hispanic or latino total")
    xcshispanic_male = models.CharField(db_column='XCSHISPM', max_length=1) 
    cs_hispanic_male = models.IntegerField(db_column='CSHISPM', verbose_name="hispanic or latino men")
    xcshispanic_female = models.CharField(db_column='XCSHISPW', max_length=1) 
    cs_hispanic_female = models.IntegerField(db_column='CSHISPW', verbose_name="hispanic or latino women")
    xcsnhpi_tot = models.CharField(db_column='XCSNHPIT', max_length=1) 
    cs_nhpi_tot = models.IntegerField(db_column='CSNHPIT', verbose_name="native hawaiian or other pacific islander total")
    xcsnhpi_male = models.CharField(db_column='XCSNHPIM', max_length=1) 
    cs_nhpi_male = models.IntegerField(db_column='CSNHPIM', verbose_name="native hawaiian or other pacific islander men")
    xcsnhpi_female = models.CharField(db_column='XCSNHPIW', max_length=1) 
    cs_nhpi_female = models.IntegerField(db_column='CSNHPIW', verbose_name="native hawaiian or other pacific islander women")
    xcstot_white = models.CharField(db_column='XCSWHITT', max_length=1) 
    cs_tot_white = models.IntegerField(db_column='CSWHITT', verbose_name="white total")
    xcswhite_male = models.CharField(db_column='XCSWHITM', max_length=1) 
    cs_white_male = models.IntegerField(db_column='CSWHITM', verbose_name="white men")
    xcs_white_female = models.CharField(db_column='XCSWHITW', max_length=1) 
    cs_white_female = models.IntegerField(db_column='CSWHITW', verbose_name="white women")
    xcs_tot_biracial = models.CharField(db_column='XCS2MORT', max_length=1) 
    cs_tot_biracial = models.IntegerField(db_column='CS2MORT', verbose_name="two or more races total")
    xcsbiracial_male = models.CharField(db_column='XCS2MORM', max_length=1) 
    cs_biracial_male = models.IntegerField(db_column='CS2MORM', verbose_name="two or more races men")
    xcsbiracial_female = models.CharField(db_column='XCS2MORW', max_length=1) 
    cs_biracial_female = models.IntegerField(db_column='CS2MORW', verbose_name="two or more races women")
    xcstot_unknown = models.CharField(db_column='XCSUNKNT', max_length=1) 
    cs_tot_unknown = models.IntegerField(db_column='CSUNKNT', verbose_name="race/ethnicity unknown total")
    xcsunknown_male = models.CharField(db_column='XCSUNKNM', max_length=1) 
    cs_unknown_male = models.IntegerField(db_column='CSUNKNM', verbose_name="race/ethnicity unknown men")
    xcsunknown_female = models.CharField(db_column='XCSUNKNW', max_length=1) 
    cs_unknown_female = models.IntegerField(db_column='CSUNKNW', verbose_name="race/ethnicity unknown women")
    xcsnralt = models.CharField(db_column='XCSNRALT', max_length=1) 
    csnralt = models.IntegerField(db_column='CSNRALT', verbose_name="nonresident alien total")
    xcsnralm = models.CharField(db_column='XCSNRALM', max_length=1) 
    csnralm = models.IntegerField(db_column='CSNRALM', verbose_name="nonresident alien men")
    xcsnralw = models.CharField(db_column='XCSNRALW', max_length=1) 
    csnralw_field = models.IntegerField(db_column='CSNRALW ') 

    class Meta:
        managed = False
        db_table = 'c2013_b'


class DegreesbyAgeEthnicity(models.Model):
    # Number of students receiving degree/certificate by award level,
    # ethnicity, gender, and age category
    unitid = models.ForeignKey('UnivBaseTable', db_column='UNITID') 
    awlevelc = models.CharField(db_column='AWLEVELC', max_length=2, verbose_name="award level code")
    xcsgrand_tot = models.CharField(db_column='XCSTOTLT', max_length=1) 
    cs_grand_tot = models.IntegerField(db_column='CSTOTLT', verbose_name="grand total")
    xcstot_male = models.CharField(db_column='XCSTOTLM', max_length=1) 
    cs_tot_male = models.IntegerField(db_column='CSTOTLM', verbose_name="grand total men")
    xcstot_female = models.CharField(db_column='XCSTOTLW', max_length=1) 
    cs_tot_female = models.IntegerField(db_column='CSTOTLW', verbose_name="grand total women")
    xcstot_aian = models.CharField(db_column='XCSAIANT', max_length=1) 
    cs_tot_aian = models.IntegerField(db_column='CSAIANT', verbose_name="american indian or alaska native total")
    xcstot_asian = models.CharField(db_column='XCSASIAT', max_length=1) 
    cs_tot_asian = models.IntegerField(db_column='CSASIAT', verbose_name="asian total")
    xcstot_black = models.CharField(db_column='XCSBKAAT', max_length=1) 
    cs_tot_black = models.IntegerField(db_column='CSBKAAT', verbose_name="black or african american total")
    xcstot_hispanic = models.CharField(db_column='XCSHISPT', max_length=1) 
    cs_tot_hispanic = models.IntegerField(db_column='CSHISPT', verbose_name="hispanic or latino total")
    xcstot_nhpi = models.CharField(db_column='XCSNHPIT', max_length=1) 
    cs_tot_nhpi = models.IntegerField(db_column='CSNHPIT', verbose_name="native hawaiian or other pacific islander total")
    xcstot_white = models.CharField(db_column='XCSWHITT', max_length=1) 
    cs_tot_white = models.IntegerField(db_column='CSWHITT', verbose_name="white total")
    xcstot_biracial = models.CharField(db_column='XCS2MORT', max_length=1) 
    cs_tot_biracial = models.IntegerField(db_column='CS2MORT', verbose_name="two or more races total")
    xcstot_unknown = models.CharField(db_column='XCSUNKNT', max_length=1) 
    cs_tot_unknown = models.IntegerField(db_column='CSUNKNT', verbose_name="race/ethnicity unknown total")
    xcsnralt = models.CharField(db_column='XCSNRALT', max_length=1) 
    csnralt = models.IntegerField(db_column='CSNRALT', verbose_name="nonresident alien total")
    xcsunder18 = models.CharField(db_column='XCSUND18', max_length=1) 
    cs_under_18 = models.IntegerField(db_column='CSUND18', verbose_name="ages, under 18")
    xcsage18_24 = models.CharField(db_column='XCS18_24', max_length=1) 
    cs_age_18_24 = models.IntegerField(db_column='CS18_24', verbose_name="ages, 18-24")
    xcsage25_39 = models.CharField(db_column='XCS25_39', max_length=1) 
    cs_age_25_39 = models.IntegerField(db_column='CS25_39', verbose_name="ages, 25-39")
    xcsabove40 = models.CharField(db_column='XCSABV40', max_length=1) 
    cs_above_40 = models.IntegerField(db_column='CSABV40', verbose_name="ages, 40 and above")
    xcsage_unknown = models.CharField(db_column='XCSUNKN', max_length=1) 
    cs_age_unknown = models.IntegerField(db_column='CSUNKN  ') 

    class Meta:
        managed = False
        db_table = 'c2013_c'


class ProgramsbyTypeLevelDistance(models.Model):
    # Number of programs offered by type, award level, and distance education
    # status
    unitid = models.ForeignKey('UnivBaseTable', db_column='UNITID') 
    cipcode = models.CharField(db_column='CIPCODE', max_length=7,verbose_name="cipcode",choices=CIPCODE_CHOICES)
    progs = models.IntegerField(db_column='PTOTAL', verbose_name="number of programs offered")
    dist_progs = models.IntegerField(db_column='PTOTALDE', verbose_name="number of programs offered via distance education")
    assoc_progs = models.IntegerField(db_column='PASSOC', verbose_name="number of associate's degree programs offered")
    dist_assoc_progs = models.IntegerField(db_column='PASSOCDE', verbose_name="number of associate's degree programs offered via distance education")
    bach_progs = models.IntegerField(db_column='PBACHL', verbose_name="number of bachelor's degree programs offered")
    dist_bach_progs = models.IntegerField(db_column='PBACHLDE', verbose_name="number of bachelor's degree programs offered via distance education")
    mast_progs = models.IntegerField(db_column='PMASTR', verbose_name="number of master's degree programs offered")
    dist_mast_progs = models.IntegerField(db_column='PMASTRDE', verbose_name="number of master's degree programs offered via distance education")
    drs_progs = models.IntegerField(db_column='PDOCRS', verbose_name="number of doctor's degree-research/scholarship programs offered")
    dist_drs_progs = models.IntegerField(db_column='PDOCRSDE', verbose_name="number of doctor's degree-research/scholarship programs offered via distance education")
    dr_pp_progs = models.IntegerField(db_column='PDOCPP', verbose_name="number of doctor's degree-professional practice programs offered")
    dist_dr_pp_progs = models.IntegerField(db_column='PDOCPPDE', verbose_name="number of doctor's degree-professional practice programs offered via distance education")
    dr_oth_progs = models.IntegerField(db_column='PDOCOT', verbose_name="number of doctor's degree-other programs offered")
    dist_dr_oth_progs = models.IntegerField(db_column='PDOCOTDE', verbose_name="number of doctor's degree-other programs offered via distance education")
    cert_prog_lt1yr = models.IntegerField(db_column='PCERT1', verbose_name="number of less than 1-year certificate programs offered")
    dist_cert_prog_lt1yr = models.IntegerField(db_column='PCERT1DE', verbose_name="number of less than 1-year certificate programs offered via distance education")
    cert_prog_lt2yr = models.IntegerField(db_column='PCERT2', verbose_name="number of 1-year, but less than-2-year certificate programs offered")
    dist_cert_prog_lt2yr = models.IntegerField(db_column='PCERT2DE', verbose_name="number of 1-year, but less than 2-year certificate programs offered via distance education")
    cert_prog_lt4yr = models.IntegerField(db_column='PCERT4', verbose_name="number of 2-year, but less than 4-year certificate programs offered")
    dist_cert_prog_lt4yr = models.IntegerField(db_column='PCERT4DE', verbose_name="number of 2-year, but less than 4-year certificate programs offered via distance education")
    post_bach_prog = models.IntegerField(db_column='PPBACC', verbose_name="number of postbaccalaureate certificate programs offered")
    dist_post_bach_prog = models.IntegerField(db_column='PPBACCDE', verbose_name="number of postbaccalaureate certificate programs offered via distance education")
    post_mstr_prog = models.IntegerField(db_column='PPMAST', verbose_name="number of post-master's certificate programs offered")
    dist_post_mstr_prog = models.IntegerField(db_column='PPMASTDE', verbose_name="number of post-master's certificate programs offered via distance education")

    class Meta:
        managed = False
        db_table = 'c2013dep'


class EnrollbyEthnAttendLevel(models.Model):
    # Number of students enrolled by ethnicity, gender, attendance status, and
    # level of student
    # ** Includes race/ethnicity - below table does not **
    unitid = models.ForeignKey('UnivBaseTable', db_column='UNITID') 
    efalevel = models.IntegerField(db_column='EFALEVEL', verbose_name="level of student", choices=EFA_LEVEL_CHOICES)
    # line = models.IntegerField(db_column='LINE', verbose_name="level of student (original line number on survey form)")
    section = models.IntegerField(db_column='SECTION', verbose_name="attendance status of student", choices=SECTION_CHOICES)
    lstudy = models.IntegerField(db_column='LSTUDY', verbose_name="level of student", choices=LSTUDY_A_CHOICES)
    xefgrand_tot = models.CharField(db_column='XEFTOTLT', max_length=1) 
    ef_grand_tot = models.IntegerField(db_column='EFTOTLT', verbose_name="grand total")
    xeftot_male = models.CharField(db_column='XEFTOTLM', max_length=1) 
    ef_tot_male = models.IntegerField(db_column='EFTOTLM', verbose_name="grand total men")
    xeftot_female = models.CharField(db_column='XEFTOTLW', max_length=1) 
    ef_tot_female = models.IntegerField(db_column='EFTOTLW', verbose_name="grand total women")
    xeftot_aian = models.CharField(db_column='XEFAIANT', max_length=1) 
    ef_tot_aian = models.IntegerField(db_column='EFAIANT', verbose_name="american indian or alaska native total")
    xefaian_male = models.CharField(db_column='XEFAIANM', max_length=1) 
    ef_aian_male = models.IntegerField(db_column='EFAIANM', verbose_name="american indian or alaska native men")
    xefaian_female = models.CharField(db_column='XEFAIANW', max_length=1) 
    ef_aian_female = models.IntegerField(db_column='EFAIANW', verbose_name="american indian or alaska native women")
    xeftot_asian = models.CharField(db_column='XEFASIAT', max_length=1) 
    ef_tot_asian = models.IntegerField(db_column='EFASIAT', verbose_name="asian total")
    xefasian_male = models.CharField(db_column='XEFASIAM', max_length=1) 
    ef_asian_male = models.IntegerField(db_column='EFASIAM', verbose_name="asian men")
    xefasian_female = models.CharField(db_column='XEFASIAW', max_length=1) 
    ef_asian_female = models.IntegerField(db_column='EFASIAW', verbose_name="asian women")
    xeftot_black = models.CharField(db_column='XEFBKAAT', max_length=1) 
    ef_tot_black = models.IntegerField(db_column='EFBKAAT', verbose_name="black or african american total")
    xefblack_male = models.CharField(db_column='XEFBKAAM', max_length=1) 
    ef_black_male = models.IntegerField(db_column='EFBKAAM', verbose_name="black or african american men")
    xefblack_female = models.CharField(db_column='XEFBKAAW', max_length=1) 
    ef_black_female = models.IntegerField(db_column='EFBKAAW', verbose_name="black or african american women")
    xeftot_hispanic = models.CharField(db_column='XEFHISPT', max_length=1) 
    ef_tot_hispanic = models.IntegerField(db_column='EFHISPT', verbose_name="hispanic total")
    xefhispanic_male = models.CharField(db_column='XEFHISPM', max_length=1) 
    ef_hispanic_male = models.IntegerField(db_column='EFHISPM', verbose_name="hispanic men")
    xefhispanic_female = models.CharField(db_column='XEFHISPW', max_length=1) 
    ef_hispanic_female = models.IntegerField(db_column='EFHISPW', verbose_name="hispanic women")
    xeftot_nhpi = models.CharField(db_column='XEFNHPIT', max_length=1) 
    ef_tot_nhpi = models.IntegerField(db_column='EFNHPIT', verbose_name="native hawaiian or other pacific islander total")
    xefnhpi_male = models.CharField(db_column='XEFNHPIM', max_length=1) 
    ef_nhpi_male = models.IntegerField(db_column='EFNHPIM', verbose_name="native hawaiian or other pacific islander men")
    xefnhpi_female = models.CharField(db_column='XEFNHPIW', max_length=1) 
    ef_nhpi_female = models.IntegerField(db_column='EFNHPIW', verbose_name="native hawaiian or other pacific islander women")
    xeftot_white = models.CharField(db_column='XEFWHITT', max_length=1) 
    ef_tot_white = models.IntegerField(db_column='EFWHITT', verbose_name="white total")
    xef_white_male = models.CharField(db_column='XEFWHITM', max_length=1) 
    ef_white_male = models.IntegerField(db_column='EFWHITM', verbose_name="white men")
    xefwhite_female = models.CharField(db_column='XEFWHITW', max_length=1) 
    ef_white_female = models.IntegerField(db_column='EFWHITW', verbose_name="white women")
    xeftot_biracial = models.CharField(db_column='XEF2MORT', max_length=1) 
    ef_tot_biracial = models.IntegerField(db_column='EF2MORT', verbose_name="two or more races total")
    xefbiracial_male = models.CharField(db_column='XEF2MORM', max_length=1) 
    ef_biracial_male = models.IntegerField(db_column='EF2MORM', verbose_name="two or more races men")
    xefbiracial_female = models.CharField(db_column='XEF2MORW', max_length=1) 
    ef_biracial_female = models.IntegerField(db_column='EF2MORW', verbose_name="two or more races women")
    xeftot_unknown = models.CharField(db_column='XEFUNKNT', max_length=1) 
    ef_tot_unknown = models.IntegerField(db_column='EFUNKNT', verbose_name="race/ethnicity unknown total")
    xefunknown_male = models.CharField(db_column='XEFUNKNM', max_length=1) 
    ef_unknown_male = models.IntegerField(db_column='EFUNKNM', verbose_name="race/ethnicity unknown men")
    xefunknown_female = models.CharField(db_column='XEFUNKNW', max_length=1) 
    ef_unknown_female = models.IntegerField(db_column='EFUNKNW', verbose_name="race/ethnicity unknown women")
    xefnralt = models.CharField(db_column='XEFNRALT', max_length=1) 
    efnralt = models.IntegerField(db_column='EFNRALT', verbose_name="nonresident alien total")
    xefnralm = models.CharField(db_column='XEFNRALM', max_length=1) 
    efnralm = models.IntegerField(db_column='EFNRALM', verbose_name="nonresident alien men")
    xefnralw = models.CharField(db_column='XEFNRALW', max_length=1) 
    efnralw_field = models.IntegerField(db_column='EFNRALW ') 

    class Meta:
        managed = False
        db_table = 'ef2013a'

class EnrollbyAgeAttendLevel(models.Model):
    # Number of students enrolled by age, gender, attendance status and level
    # of student
    unitid = models.ForeignKey('UnivBaseTable', db_column='UNITID') 
    efbage = models.IntegerField(db_column='EFBAGE', verbose_name="age category")
    line = models.IntegerField(db_column='LINE', verbose_name="level of student (original line number on survey form)")
    lstudy = models.IntegerField(db_column='LSTUDY', verbose_name="level of student", choices = LSTUDY_B_CHOICES)
    xefft_male = models.CharField(db_column='XEFAGE01', max_length=1) 
    ef_ft_male = models.IntegerField(db_column='EFAGE01', verbose_name="full time men")
    xefft_female = models.CharField(db_column='XEFAGE02', max_length=1) 
    ef_ft_female = models.IntegerField(db_column='EFAGE02', verbose_name="full time women")
    xefpt_male = models.CharField(db_column='XEFAGE03', max_length=1) 
    ef_pt_male = models.IntegerField(db_column='EFAGE03', verbose_name="part time men")
    xefpt_female = models.CharField(db_column='XEFAGE04', max_length=1) 
    ef_pt_female = models.IntegerField(db_column='EFAGE04', verbose_name="part time women")
    xeftot_ft = models.CharField(db_column='XEFAGE05', max_length=1) 
    ef_tot_ft = models.IntegerField(db_column='EFAGE05', verbose_name="full time total")
    xeftot_pt = models.CharField(db_column='XEFAGE06', max_length=1) 
    ef_tot_pt = models.IntegerField(db_column='EFAGE06', verbose_name="part time total")
    xeftot_male = models.CharField(db_column='XEFAGE07', max_length=1) 
    ef_tot_male = models.IntegerField(db_column='EFAGE07', verbose_name="total men")
    xeftot_female = models.CharField(db_column='XEFAGE08', max_length=1) 
    ef_tot_female = models.IntegerField(db_column='EFAGE08', verbose_name="total women")
    xefgrand_tot = models.CharField(db_column='XEFAGE09', max_length=1) 
    ef_grand_tot = models.IntegerField(db_column='EFAGE09 ') 

    class Meta:
        managed = False
        db_table = 'ef2013b'


class FirstTimeResidMigration(models.Model):
    # FIRST-TIME FRESHMAN DATA
    unitid = models.ForeignKey('UnivBaseTable', db_column='UNITID') 
    efcstate = models.IntegerField(db_column='EFCSTATE', verbose_name="state of residence when student was first admitted", choices=EFC_STATE_CHOICES)
    line = models.IntegerField(db_column='LINE', verbose_name="level of student (original line number on survey form)")
    xefres01 = models.CharField(db_column='XEFRES01', max_length=1) 
    efres01 = models.IntegerField(db_column='EFRES01', verbose_name="first-time degree/certificate-seeking undergraduate students")
    xefres02 = models.CharField(db_column='XEFRES02', max_length=1) 
    efres02_field = models.IntegerField(db_column='EFRES02 ', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'ef2013c'


class IncomingClassRetentionRatios(models.Model):
    # Current entering class (not full university), retention rate
    unitid = models.ForeignKey('UnivBaseTable', db_column='UNITID') 
    xgrcohrt = models.CharField(db_column='XGRCOHRT', max_length=1) 
    grcohrt = models.IntegerField(db_column='GRCOHRT', blank=True, null=True, verbose_name="full-time first-time degree/certificate-seeking undergraduate (current year grs cohort)")
    xugenter = models.CharField(db_column='XUGENTER', max_length=1) 
    ugentern = models.IntegerField(db_column='UGENTERN', blank=True, null=True, verbose_name="total entering students at the undergraduate level, fall 2013")
    xpgrcohr = models.CharField(db_column='XPGRCOHR', max_length=1) 
    pgrcohrt = models.IntegerField(db_column='PGRCOHRT', blank=True, null=True, verbose_name="current year grs cohort as a percent of entering class")
    xrrftct = models.CharField(db_column='XRRFTCT', max_length=1) 
    rrftct = models.IntegerField(db_column='RRFTCT', blank=True, null=True, verbose_name="full-time fall 2012 cohort")
    xrrftex = models.CharField(db_column='XRRFTEX', max_length=1) 
    rrftex = models.IntegerField(db_column='RRFTEX', blank=True, null=True, verbose_name="exclusions from full-time fall 2012 cohort")
    xrrftcta = models.CharField(db_column='XRRFTCTA', max_length=1) 
    rrftcta = models.IntegerField(db_column='RRFTCTA', blank=True, null=True, verbose_name="full-time adjusted fall 2012 cohort")
    xret_nmf = models.CharField(db_column='XRET_NMF', max_length=1) 
    ret_nmf = models.IntegerField(db_column='RET_NMF', blank=True, null=True, verbose_name="students from the full-time adjusted fall 2012 cohort enrolled in fall 2013")
    xret_pcf = models.CharField(db_column='XRET_PCF', max_length=1) 
    ret_pcf = models.IntegerField(db_column='RET_PCF', blank=True, null=True, verbose_name="full-time retention rate, 2013")
    xrrptct = models.CharField(db_column='XRRPTCT', max_length=1) 
    rrptct = models.IntegerField(db_column='RRPTCT', blank=True, null=True, verbose_name="part-time fall 2012 cohort")
    xrrptex = models.CharField(db_column='XRRPTEX', max_length=1) 
    rrptex = models.IntegerField(db_column='RRPTEX', blank=True, null=True, verbose_name="exclusions from part-time fall 2012 cohort")
    xrrptcta = models.CharField(db_column='XRRPTCTA', max_length=1) 
    rrptcta = models.IntegerField(db_column='RRPTCTA', blank=True, null=True, verbose_name="part-time adjusted fall 2012 cohort")
    xret_nmp = models.CharField(db_column='XRET_NMP', max_length=1) 
    ret_nmp = models.IntegerField(db_column='RET_NMP', blank=True, null=True, verbose_name="students from the part-time adjusted fall 2012 cohort enrolled in fall 2013")
    xret_pcp = models.CharField(db_column='XRET_PCP', max_length=1) 
    ret_pcp = models.IntegerField(db_column='RET_PCP', blank=True, null=True, verbose_name="part-time retention rate, 2013")
    xstufacr = models.CharField(db_column='XSTUFACR', max_length=1) 
    stufacr_field = models.IntegerField(db_column='STUFACR ', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'ef2013d'


class SurveyCompletionStatus(models.Model):
    # Indicates whether universities responded to the survey, whether the
    # responses include both parent/child campuses, etc.
    unitid = models.ForeignKey('UnivBaseTable', db_column='UNITID') 
    stat_ic = models.IntegerField(db_column='STAT_IC', verbose_name="response status -  institutional characteristics component")
    lock_ic = models.IntegerField(db_column='LOCK_IC', verbose_name="status of ic component when institution was migrated")
    imp_ic = models.IntegerField(db_column='IMP_IC', verbose_name="type of imputation method institutional characteristics")
    stat_c = models.IntegerField(db_column='STAT_C', verbose_name="response status -  completions component")
    lock_c = models.IntegerField(db_column='LOCK_C', verbose_name="status of completions component when institution was migrated")
    prch_c = models.IntegerField(db_column='PRCH_C', verbose_name="parent/child indicator for completions")
    idx_c = models.IntegerField(db_column='IDX_C', verbose_name="unitid of parent institution")
    pcc_f = models.IntegerField(db_column='PCC_F', blank=True, null=True, verbose_name="parent/child allocation factor - completions")
    imp_c = models.IntegerField(db_column='IMP_C', verbose_name="type of imputation method completions")
    stat_e12 = models.IntegerField(db_column='STAT_E12', verbose_name="response status of institution - 12-month enrollment")
    lock_e12 = models.IntegerField(db_column='LOCK_E12', verbose_name="status of 12-month enrollment component whe data collection closed")
    prch_e12 = models.IntegerField(db_column='PRCH_E12', verbose_name="parent/child indicator for 12-month enrollment")
    idx_e12 = models.IntegerField(db_column='IDX_E12', verbose_name="id number of parent institution - 12-month enrollment")
    pce12_f = models.CharField(db_column='PCE12_F', max_length=32, blank=True, null=True, verbose_name="parent/child allocation factor - 12-month enrollment")
    imp_e12 = models.IntegerField(db_column='IMP_E12', verbose_name="type of imputation method - 12 month enrollment")
    stat_hr = models.IntegerField(db_column='STAT_HR', verbose_name="response status of institution for human resources (hr) component")
    lock_hr = models.IntegerField(db_column='LOCK_HR', verbose_name="status of human resources (hr) component when data collection closed")
    prch_hr = models.IntegerField(db_column='PRCH_HR', verbose_name="parent/child  indicator - human resources (hr) component")
    idx_hr = models.IntegerField(db_column='IDX_HR', verbose_name="id of institution where data are reported for the human resources (hr) component")
    pchr_f = models.IntegerField(db_column='PCHR_F', blank=True, null=True, verbose_name="parent/child allocation factor - hr")
    imp_hr = models.IntegerField(db_column='IMP_HR', verbose_name="type of imputation method - human resources (hr) component")
    ftemp15 = models.IntegerField(db_column='FTEMP15', verbose_name="does institution have 15 or more full-time employees")
    tenursys = models.IntegerField(db_column='TENURSYS', verbose_name="does institution have a tenure system")
    sa_excl = models.IntegerField(db_column='SA_EXCL', verbose_name="salary exclusion")
    stat_eap = models.IntegerField(db_column='STAT_EAP', verbose_name="response status for eap")
    stat_sa = models.IntegerField(db_column='STAT_SA', verbose_name="response status to sa survey")
    stat_s = models.IntegerField(db_column='STAT_S', verbose_name="response status for fall staff")
    stat_ef = models.IntegerField(db_column='STAT_EF', verbose_name="response status of institution -  fall enrollment")
    lock_ef = models.IntegerField(db_column='LOCK_EF', verbose_name="status of fall enrollment survey when data collection closed")
    prch_ef = models.IntegerField(db_column='PRCH_EF', verbose_name="parent/child indicator f- fall enrollment")
    idx_ef = models.IntegerField(db_column='IDX_EF', verbose_name="id number of parent institution - fall enrollment")
    pcef_f = models.IntegerField(db_column='PCEF_F', blank=True, null=True, verbose_name="parent/child allocation factor - fall enrollment")
    imp_ef = models.IntegerField(db_column='IMP_EF', verbose_name="type of imputation method - fall enrollment")
    pta99_ef = models.IntegerField(db_column='PTA99_EF', verbose_name="status enrollment by race/ethnicity (99.0000 cip)")
    ptacipef = models.IntegerField(db_column='PTACIPEF', verbose_name="status enrollment by major")
    ptb_ef = models.IntegerField(db_column='PTB_EF', verbose_name="status enrollment summary by age")
    ptc_ef = models.IntegerField(db_column='PTC_EF', verbose_name="status residence of first-time first-year students")
    ptd_ef = models.IntegerField(db_column='PTD_EF', verbose_name="status total entering class and retention rates")
    form_f = models.IntegerField(db_column='FORM_F', verbose_name="identifies reporting standards gasb, fasb, or modified fasb(for-profit institutions) used to report finance data")
    stat_f = models.IntegerField(db_column='STAT_F', verbose_name="response status for finance survey")
    lock_f = models.IntegerField(db_column='LOCK_F', verbose_name="status of finance survey when data collection closed")
    prch_f = models.IntegerField(db_column='PRCH_F', verbose_name="parent/child indicator for finance survey")
    idx_f = models.IntegerField(db_column='IDX_F', verbose_name="id number of parent institution for finance survey")
    pcf_f = models.FloatField(db_column='PCF_F', blank=True, null=True, verbose_name="parent/child allocation factor - finance")
    imp_f = models.IntegerField(db_column='IMP_F', verbose_name="type of imputation method  finance")
    fybeg = models.CharField(db_column='FYBEG', max_length=6, verbose_name="beginning date of fiscal year covered (all finance)")
    fyend = models.CharField(db_column='FYEND', max_length=6, verbose_name="end date of fiscal year covered  (all finance)")
    gpfs = models.IntegerField(db_column='GPFS', verbose_name="clean opinion gpfs from auditor (all finance)")
    f1gasbal = models.IntegerField(db_column='F1GASBAL', verbose_name="gasb alternative accounting model")
    f2pell = models.IntegerField(db_column='F2PELL', verbose_name="account for pell grants as pass through transactions or as federal grant revenues to the institution (fasb  institutions)?")
    f3pell = models.IntegerField(db_column='F3PELL', verbose_name="account for pell grants as pass through transactions or as federal grant revenues to the institution (private-for-profit institutions)?")
    f_athltc = models.IntegerField(db_column='F_ATHLTC', verbose_name="are intercollegiate athletic expenses accounted for as auxiliary enterprises or treated as student services?")
    stat_sfa = models.IntegerField(db_column='STAT_SFA', verbose_name="response status for student financial aid survey")
    lock_sfa = models.IntegerField(db_column='LOCK_SFA', verbose_name="status of student financial aid survey when data collection closed")
    prch_sfa = models.IntegerField(db_column='PRCH_SFA', verbose_name="parent/child indicator student financial aid survey")
    idx_sfa = models.IntegerField(db_column='IDX_SFA', verbose_name="id number of parent institution student financial aid")
    pcsfa_f = models.IntegerField(db_column='PCSFA_F', blank=True, null=True, verbose_name="parent/child allocation factor - student financial aid")
    imp_sfa = models.IntegerField(db_column='IMP_SFA', verbose_name="type of imputation method student financial aid")
    stat_gr = models.IntegerField(db_column='STAT_GR', verbose_name="response status - graduation rates")
    lock_gr = models.IntegerField(db_column='LOCK_GR', verbose_name="status of graduation rate survey when data collection closed")
    prch_gr = models.IntegerField(db_column='PRCH_GR', verbose_name="parent/child indicator - graduation rates")
    idx_gr = models.IntegerField(db_column='IDX_GR', verbose_name="unitid of parent institution reporting graduation rates")
    pcgr_f = models.IntegerField(db_column='PCGR_F', blank=True, null=True, verbose_name="parent/child allocation factor - graduation rates")
    imp_gr = models.IntegerField(db_column='IMP_GR', verbose_name="imputation method - graduation rates")
    cohrtstu = models.IntegerField(db_column='COHRTSTU', verbose_name="enrolled any full-time first-time students")
    hasgrurl = models.IntegerField(db_column='HASGRURL', verbose_name="does institution use a website to disclose student-right-to-know student athlete graduation rates")
    grdisurl = models.CharField(db_column='GRDISURL', max_length=150, blank=True, null=True, verbose_name="student-right-to-know student athlete graduation rate website url")
    stat_gr2 = models.IntegerField(db_column='STAT_GR2', verbose_name="response status - graduation rates 200")
    lock_gr2 = models.IntegerField(db_column='LOCK_GR2', verbose_name="status of graduation rate 200 survey when data collection closed")
    prch_gr2 = models.IntegerField(db_column='PRCH_GR2', verbose_name="parent/child indicator - graduation rates 200")
    idx_gr2 = models.IntegerField(db_column='IDX_GR2', verbose_name="unitid of parent institution reporting graduation rates 200")
    imp_gr2 = models.IntegerField(db_column='IMP_GR2', verbose_name="imputation method - graduation rates 200")
    ntrldstr = models.IntegerField(db_column='NTRLDSTR', verbose_name="natural disaster identification")

    class Meta:
        managed = False
        db_table = 'flags2013'


class GraduationRates4Yr(models.Model):
    # Graduation rates for 4-year institutions
    unitid = models.OneToOneField('UnivBaseTable', db_column='UNITID',related_name='gradrate') 
    xbarevct = models.CharField(db_column='XBAREVCT', max_length=1) 
    barevct = models.IntegerField(db_column='BAREVCT', blank=True, null=True, verbose_name="revised bachelor's degree-seeking cohort, (cohort year 2005)")
    xbaexclu = models.CharField(db_column='XBAEXCLU', max_length=1) 
    baexclu = models.IntegerField(db_column='BAEXCLU', blank=True, null=True, verbose_name="exclusions from bachelor's degree-seeking cohort within 150% percent of normal time")
    xbaac150 = models.CharField(db_column='XBAAC150', max_length=1) 
    baac150 = models.IntegerField(db_column='BAAC150', blank=True, null=True, verbose_name="adjusted bachelor's degree-seeking cohort within 150% of normal time")
    xbanc100 = models.CharField(db_column='XBANC100', max_length=1) 
    bachdegrees_100 = models.IntegerField(db_column='BANC100', blank=True, null=True, verbose_name="number completed a bachelor's degree within 100% of normal time (4-years)")
    xbagr100 = models.CharField(db_column='XBAGR100', max_length=1) 
    bach_gradrate_100 = models.IntegerField(db_column='BAGR100', blank=True, null=True, verbose_name="4-year graduation rate - bachelor's degree within 100% of normal time")
    xbanc150 = models.CharField(db_column='XBANC150', max_length=1) 
    bachdegrees_150 = models.IntegerField(db_column='BANC150', blank=True, null=True, verbose_name="number completed a bachelor's degree within 150% of normal time (6-years)")
    xbagr150 = models.CharField(db_column='XBAGR150', max_length=1) 
    bach_gradrate_150 = models.IntegerField(db_column='BAGR150', blank=True, null=True, verbose_name="6-year graduation rate - bachelor's degree within 150% of normal time")
    xbaaexcl = models.CharField(db_column='XBAAEXCL', max_length=1) 
    baaexcl = models.IntegerField(db_column='BAAEXCL', blank=True, null=True, verbose_name="additional exclusions from bachelor's degree-seeking cohort")
    xbaac200 = models.CharField(db_column='XBAAC200', max_length=1) 
    baac200 = models.IntegerField(db_column='BAAC200', blank=True, null=True, verbose_name="adjusted bachelor's degree-seeking cohort within 200% of normal time")
    xbanc20a = models.CharField(db_column='XBANC20A', max_length=1) 
    banc200a = models.IntegerField(db_column='BANC200A', blank=True, null=True, verbose_name="number completed a bachelor's degree between 150% and 200% of normal time")
    xbastend = models.CharField(db_column='XBASTEND', max_length=1) 
    still_enrolled = models.IntegerField(db_column='BASTEND', blank=True, null=True, verbose_name="still enrolled")
    xbanc200 = models.CharField(db_column='XBANC200', max_length=1) 
    bachdegrees_200 = models.IntegerField(db_column='BANC200', blank=True, null=True, verbose_name="number completed a bachelor's degree within 200% of normal time (8-years)")
    xbagr200 = models.CharField(db_column='XBAGR200', max_length=1) 
    bach_gradrate_200 = models.IntegerField(db_column='BAGR200', blank=True, null=True, verbose_name="8-year graduation rate - bachelor's degree within 200% of normal time")
    xl4revct = models.CharField(db_column='XL4REVCT', max_length=1) 
    l4revct = models.IntegerField(db_column='L4REVCT', blank=True, null=True, verbose_name="revised degree/certificate-seeking cohort, (cohort year 2009)")
    xl4exclu = models.CharField(db_column='XL4EXCLU', max_length=1) 
    l4exclu = models.IntegerField(db_column='L4EXCLU', blank=True, null=True, verbose_name="exclusions from degree/certificate-seeking cohort within 150% percent of normal time")
    xl4ac150 = models.CharField(db_column='XL4AC150', max_length=1) 
    l4ac150 = models.IntegerField(db_column='L4AC150', blank=True, null=True, verbose_name="adjusted degree/certificate-seeking cohort within 150% of normal time")
    xl4nc100 = models.CharField(db_column='XL4NC100', max_length=1) 
    l4nc100 = models.IntegerField(db_column='L4NC100', blank=True, null=True, verbose_name="number completed a degree/certificate within 100% of normal time")
    xl4gr100 = models.CharField(db_column='XL4GR100', max_length=1) 
    l4gr100 = models.IntegerField(db_column='L4GR100', blank=True, null=True, verbose_name="graduation rate - degree/certificate within 100% of normal time")
    xl4nc150 = models.CharField(db_column='XL4NC150', max_length=1) 
    l4nc150 = models.IntegerField(db_column='L4NC150', blank=True, null=True, verbose_name="number completed a degree/certificate  within 150% of normal time")
    xl4gr150 = models.CharField(db_column='XL4GR150', max_length=1) 
    l4gr150 = models.IntegerField(db_column='L4GR150', blank=True, null=True, verbose_name="graduation rate - degree/certificate within 150% of normal time")
    xl4aexcl = models.CharField(db_column='XL4AEXCL', max_length=1) 
    l4aexcl = models.IntegerField(db_column='L4AEXCL', blank=True, null=True, verbose_name="additional exclusions from degree/certificate-seeking cohort")
    xl4ac200 = models.CharField(db_column='XL4AC200', max_length=1) 
    l4ac200 = models.IntegerField(db_column='L4AC200', blank=True, null=True, verbose_name="adjusted degree/certificate-seeking cohort within 200% of normal time")
    xl4nc20a = models.CharField(db_column='XL4NC20A', max_length=1) 
    l4nc200a = models.IntegerField(db_column='L4NC200A', blank=True, null=True, verbose_name="number completed a  degree/certificate between 150% and 200% of normal time")
    xl4stend = models.CharField(db_column='XL4STEND', max_length=1) 
    l4stend = models.IntegerField(db_column='L4STEND', blank=True, null=True, verbose_name="still enrolled")
    xl4nc200 = models.CharField(db_column='XL4NC200', max_length=1) 
    l4nc200 = models.IntegerField(db_column='L4NC200', blank=True, null=True, verbose_name="number completed a degree/certificate within 200% of normal time")
    xl4gr200 = models.CharField(db_column='XL4GR200', max_length=1) 
    l4gr200_field = models.IntegerField(db_column='L4GR200 ', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'gr200_13'


class GraduationRates2Yr(models.Model):
    # Graduation rates for 2-year institutions
    unitid = models.ForeignKey('UnivBaseTable', db_column='UNITID') 
    xline_10 = models.CharField(db_column='XLINE_10', max_length=1) 
    line_10 = models.IntegerField(db_column='LINE_10', verbose_name="revised cohort")
    xline_45 = models.CharField(db_column='XLINE_45', max_length=1) 
    line_45 = models.IntegerField(db_column='LINE_45', verbose_name="exclusions")
    xline_50 = models.CharField(db_column='XLINE_50', max_length=1) 
    line_50 = models.IntegerField(db_column='LINE_50', verbose_name="adjusted cohort (revised cohort minus exclusions)")
    xline_55 = models.CharField(db_column='XLINE_55', max_length=1) 
    line_55 = models.IntegerField(db_column='LINE_55', verbose_name="completers within 100% of normal time")
    xline_11 = models.CharField(db_column='XLINE_11', max_length=1) 
    line_11 = models.IntegerField(db_column='LINE_11', verbose_name="completers within 150% of normal time")
    xline_30 = models.CharField(db_column='XLINE_30', max_length=1) 
    line_30 = models.IntegerField(db_column='LINE_30', verbose_name="transfer-out students")
    xline_51 = models.CharField(db_column='XLINE_51', max_length=1) 
    line_51 = models.IntegerField(db_column='LINE_51', verbose_name="still enrolled")
    xline_52 = models.CharField(db_column='XLINE_52', max_length=1) 
    line_52_field = models.IntegerField(db_column='LINE_52 ') 

    class Meta:
        managed = False
        db_table = 'gr2013_l2'


class UnivBaseTable(models.Model):
    # Base table - directory info for every institution
    unitid = models.IntegerField(db_column='UNITID', primary_key=True,verbose_name="unique identification number of the institution")
    school_name = models.CharField(db_column='INSTNM', max_length=91, verbose_name="institution (entity) name")
    address = models.CharField(db_column='ADDR', max_length=76, blank=True, null=True, verbose_name="street address or post office box")
    city = models.CharField(db_column='CITY', max_length=24, verbose_name="city location of institution")
    state = models.CharField(db_column='STABBR', max_length=2,
            verbose_name="state abbreviation", choices=STATE_ABBR)
    zipcode = models.CharField(db_column='ZIP', max_length=10, verbose_name="zip code")
    fips_stcode = models.IntegerField(db_column='FIPS', verbose_name="fips state code")
    geog_region = models.IntegerField(db_column='OBEREG', verbose_name="geographic region")
    chief_admin = models.CharField(db_column='CHFNM', max_length=45, blank=True, null=True, verbose_name="name of chief administrator")
    chief_title = models.CharField(db_column='CHFTITLE', max_length=50, blank=True, null=True, verbose_name="title of chief administrator")
    tel_num = models.BigIntegerField(db_column='GENTELE', blank=True, null=True, verbose_name="general information telephone number")
    fax_num = models.BigIntegerField(db_column='FAXTELE', blank=True, null=True, verbose_name="fax number")
    employ_id = models.CharField(db_column='EIN', max_length=9, verbose_name="employer identification number")
    ope_id = models.CharField(db_column='OPEID', max_length=8, verbose_name="office of postsecondary education (ope) id number")
    ope_title4 = models.IntegerField(db_column='OPEFLAG', verbose_name="ope title iv eligibility indicator code")
    main_web = models.CharField(db_column='WEBADDR', max_length=86, blank=True, null=True, verbose_name="institution's internet website address")
    admin_web = models.CharField(db_column='ADMINURL', max_length=141, blank=True, null=True, verbose_name="admissions office web address")
    fin_aid_web = models.CharField(db_column='FAIDURL', max_length=143, blank=True, null=True, verbose_name="financial aid office web address")
    app_web = models.CharField(db_column='APPLURL', max_length=150, blank=True, null=True, verbose_name="online application web address")
    net_price_web = models.CharField(db_column='NPRICURL', max_length=143, blank=True, null=True, verbose_name="net price calculator web address")
    sector = models.IntegerField(db_column='SECTOR', verbose_name="sector of institution")
    program_length = models.IntegerField(db_column='ICLEVEL', verbose_name="level of institution")
    control = models.IntegerField(db_column='CONTROL', verbose_name="control of institution")
    hloffer = models.IntegerField(db_column='HLOFFER', verbose_name="highest level of offering")
    undergrad = models.IntegerField(db_column='UGOFFER', verbose_name="undergraduate offering")
    graduate = models.IntegerField(db_column='GROFFER', verbose_name="graduate offering")
    hdegofr1 = models.IntegerField(db_column='HDEGOFR1', verbose_name="highest degree offered")
    deg_grant_status = models.IntegerField(db_column='DEGGRANT', verbose_name="degree-granting status")
    hist_black_univ = models.IntegerField(db_column='HBCU', verbose_name="historically black college or university")
    hospital = models.IntegerField(db_column='HOSPITAL', verbose_name="institution has hospital")
    medical = models.IntegerField(db_column='MEDICAL', verbose_name="institution grants a medical degree")
    tribal = models.IntegerField(db_column='TRIBAL', verbose_name="tribal college")
    locale = models.IntegerField(db_column='LOCALE', verbose_name="degree of urbanization (urban-centric locale)")
    openpubl = models.IntegerField(db_column='OPENPUBL', verbose_name="institution open to the general public")
    IPEDS_part_status = models.CharField(db_column='ACT', max_length=1, verbose_name="status of institution")
    merged_unitid = models.IntegerField(db_column='NEWID', verbose_name="unitid for merged schools")
    year_deleted = models.IntegerField(db_column='DEATHYR', verbose_name="year institution was deleted from ipeds")
    year_closed = models.CharField(db_column='CLOSEDAT', max_length=10, verbose_name="date institution closed")
    current_year_status = models.IntegerField(db_column='CYACTIVE', verbose_name="institution is active in current year")
    postsec = models.IntegerField(db_column='POSTSEC', verbose_name="primarily postsecondary indicator")
    pseflag = models.IntegerField(db_column='PSEFLAG', verbose_name="postsecondary institution indicator")
    pset4flg = models.IntegerField(db_column='PSET4FLG', verbose_name="postsecondary and title iv institution indicator")
    rptmth = models.IntegerField(db_column='RPTMTH', verbose_name="reporting method for student charges, graduation rates, retention rates and student financial aid")
    ialias = models.CharField(db_column='IALIAS', max_length=680, blank=True, null=True, verbose_name="institution name alias")
    school_catg = models.IntegerField(db_column='INSTCAT', verbose_name="institutional category")
    carnegie_basic = models.IntegerField(db_column='CCBASIC', verbose_name="carnegie classification 2010: basic")
    carnegie_underg = models.IntegerField(db_column='CCIPUG', verbose_name="carnegie classification 2010: undergraduate instructional program")
    carnegie_grad = models.IntegerField(db_column='CCIPGRAD', verbose_name="carnegie classification 2010: graduate instructional program")
    carnegie_ugprof = models.IntegerField(db_column='CCUGPROF', verbose_name="carnegie classification 2010: undergraduate profile")
    carnegie_enrol_prof = models.IntegerField(db_column='CCENRPRF', verbose_name="carnegie classification 2010: enrollment profile")
    carnegie_size = models.IntegerField(db_column='CCSIZSET', verbose_name="carnegie classification 2010: size and setting")
    carnegie = models.IntegerField(db_column='CARNEGIE', verbose_name="carnegie classification 2000")
    landgrnt = models.IntegerField(db_column='LANDGRNT', verbose_name="land grant institution")
    instsize = models.IntegerField(db_column='INSTSIZE', verbose_name="institution size category")
    cbsa = models.IntegerField(db_column='CBSA', verbose_name="core based statistical area (cbsa)")
    cbsatype = models.IntegerField(db_column='CBSATYPE', verbose_name="cbsa type metropolitan or micropolitan")
    csa = models.IntegerField(db_column='CSA', verbose_name="combined statistical area (csa)")
    necta = models.IntegerField(db_column='NECTA', verbose_name="new england city and town area (necta)")
    f1systyp = models.IntegerField(db_column='F1SYSTYP', verbose_name="multi-institution or multi-campus organization")
    f1sysnam = models.CharField(db_column='F1SYSNAM', max_length=62, blank=True, null=True, verbose_name="name of multi-institution or multi-campus organization")
    f1syscod = models.IntegerField(db_column='F1SYSCOD', verbose_name="identification number of multi-institution or multi-campus organization")
    countycd = models.IntegerField(db_column='COUNTYCD', verbose_name="fips county code")
    countynm = models.CharField(db_column='COUNTYNM', max_length=28, verbose_name="county name")
    cngdstcd = models.IntegerField(db_column='CNGDSTCD', verbose_name="congressional district code")
    longitude = models.FloatField(db_column='LONGITUD', verbose_name="longitude location of institution")
    latitude = models.FloatField(db_column='LATITUDE', verbose_name="latitude location of institution")
    dfrcgid = models.IntegerField(db_column='DFRCGID', verbose_name="data feedback report comparison group category created by nces")
    dfrcuscg = models.IntegerField(db_column='DFRCUSCG', verbose_name="data feedback report - institution submitted a custom comparison group")

    def __str__(self):
        return self.school_name

    class Meta:
        managed = False
        db_table = 'hd2013'
        ordering = ['school_name']


class InstitutionalChars(models.Model):
    # Institutional characteristics: award levels/degrees offered, applicant/
    # admissions/ test scores
    unitid = models.OneToOneField('UnivBaseTable', db_column='UNITID', verbose_name="unique identification number of the institution", related_name="instchars")
    peo1istr = models.IntegerField(db_column='PEO1ISTR', verbose_name="occupational")
    peo2istr = models.IntegerField(db_column='PEO2ISTR', verbose_name="academic")
    peo3istr = models.IntegerField(db_column='PEO3ISTR', verbose_name="continuing professional")
    peo4istr = models.IntegerField(db_column='PEO4ISTR', verbose_name="recreational or avocational")
    peo5istr = models.IntegerField(db_column='PEO5ISTR', verbose_name="adult basic remedial or high school equivalent")
    peo6istr = models.IntegerField(db_column='PEO6ISTR', verbose_name="secondary (high school)")
    cntlaffi = models.IntegerField(db_column='CNTLAFFI', verbose_name="institutional control or affiliation")
    pubprime = models.IntegerField(db_column='PUBPRIME', verbose_name="primary public control")
    pubsecon = models.IntegerField(db_column='PUBSECON', verbose_name="secondary public control")
    relaffil = models.IntegerField(db_column='RELAFFIL', verbose_name="religious affiliation")
    level1 = models.IntegerField(db_column='LEVEL1', verbose_name="less than one year certificate")
    level2 = models.IntegerField(db_column='LEVEL2', verbose_name="one but less than two years certificate")
    level3 = models.IntegerField(db_column='LEVEL3', verbose_name="associate's degree")
    level4 = models.IntegerField(db_column='LEVEL4', verbose_name="two but less than 4 years certificate")
    level5 = models.IntegerField(db_column='LEVEL5', verbose_name="bachelor's degree")
    level6 = models.IntegerField(db_column='LEVEL6', verbose_name="postbaccalaureate certificate")
    level7 = models.IntegerField(db_column='LEVEL7', verbose_name="master's degree")
    level8 = models.IntegerField(db_column='LEVEL8', verbose_name="post-master's certificate")
    level12 = models.IntegerField(db_column='LEVEL12', verbose_name="other degree")
    level17 = models.IntegerField(db_column='LEVEL17', verbose_name="doctor's degree - research/scholarship")
    level18 = models.IntegerField(db_column='LEVEL18', verbose_name="doctor's degree - professional practice")
    level19 = models.IntegerField(db_column='LEVEL19', verbose_name="doctor's degree - other")
    openadmp = models.IntegerField(db_column='OPENADMP', verbose_name="open admission policy")
    admcon1 = models.IntegerField(db_column='ADMCON1', verbose_name="secondary school gpa")
    admcon2 = models.IntegerField(db_column='ADMCON2', verbose_name="secondary school rank")
    admcon3 = models.IntegerField(db_column='ADMCON3', verbose_name="secondary school record")
    admcon4 = models.IntegerField(db_column='ADMCON4', verbose_name="completion of college-preparatory program")
    admcon5 = models.IntegerField(db_column='ADMCON5', verbose_name="recommendations")
    admcon6 = models.IntegerField(db_column='ADMCON6', verbose_name="formal demonstration of competencies")
    admcon7 = models.IntegerField(db_column='ADMCON7', verbose_name="admission test scores")
    admcon8 = models.IntegerField(db_column='ADMCON8', verbose_name="toefl (test of english as a foreign language")
    admcon9 = models.IntegerField(db_column='ADMCON9', verbose_name="other test (wonderlic, wisc-iii, etc.)")
    appdate = models.IntegerField(db_column='APPDATE', verbose_name="fall reporting period for applicant and admissions")
    xapplcnm = models.CharField(db_column='XAPPLCNM', max_length=1) 
    applcnm = models.IntegerField(db_column='APPLCNM', blank=True, null=True, verbose_name="applicants men")
    xapplcnw = models.CharField(db_column='XAPPLCNW', max_length=1) 
    applcnw = models.IntegerField(db_column='APPLCNW', blank=True, null=True, verbose_name="applicants women")
    xadmssnm = models.CharField(db_column='XADMSSNM', max_length=1) 
    admssnm = models.IntegerField(db_column='ADMSSNM', blank=True, null=True, verbose_name="admissions men")
    xadmssnw = models.CharField(db_column='XADMSSNW', max_length=1) 
    admssnw = models.IntegerField(db_column='ADMSSNW', blank=True, null=True, verbose_name="admissions women")
    xenrlftm = models.CharField(db_column='XENRLFTM', max_length=1) 
    enrlftm = models.IntegerField(db_column='ENRLFTM', blank=True, null=True, verbose_name="enrolled full time men")
    xenrlftw = models.CharField(db_column='XENRLFTW', max_length=1) 
    enrlftw = models.IntegerField(db_column='ENRLFTW', blank=True, null=True, verbose_name="enrolled full time women")
    xenrlptm = models.CharField(db_column='XENRLPTM', max_length=1) 
    enrlptm = models.IntegerField(db_column='ENRLPTM', blank=True, null=True, verbose_name="enrolled part time men")
    xenrlptw = models.CharField(db_column='XENRLPTW', max_length=1) 
    enrlptw = models.IntegerField(db_column='ENRLPTW', blank=True, null=True, verbose_name="enrolled part time women")
    satactdt = models.IntegerField(db_column='SATACTDT', verbose_name="fall reporting period for sat/act test scores")
    xsatnum = models.CharField(db_column='XSATNUM', max_length=1) 
    satnum = models.IntegerField(db_column='SATNUM', blank=True, null=True, verbose_name="number of first-time degree/certificate-seeking students submitting sat scores")
    xsatpct = models.CharField(db_column='XSATPCT', max_length=1) 
    satpct = models.IntegerField(db_column='SATPCT', blank=True, null=True, verbose_name="percent of first-time degree/certificate-seeking students submitting sat scores")
    xactnum = models.CharField(db_column='XACTNUM', max_length=1) 
    actnum = models.IntegerField(db_column='ACTNUM', blank=True, null=True, verbose_name=" number of first-time degree/certificate-seeking students submitting act scores")
    xactpct = models.CharField(db_column='XACTPCT', max_length=1) 
    actpct = models.IntegerField(db_column='ACTPCT', blank=True, null=True, verbose_name="percent of first-time degree/certificate-seeking students submitting act scores")
    xsatvr25 = models.CharField(db_column='XSATVR25', max_length=1) 
    satvr25 = models.IntegerField(db_column='SATVR25', blank=True, null=True, verbose_name="sat critical reading 25th percentile score")
    xsatvr75 = models.CharField(db_column='XSATVR75', max_length=1) 
    satvr75 = models.IntegerField(db_column='SATVR75', blank=True, null=True, verbose_name="sat critical reading 75th percentile score")
    xsatmt25 = models.CharField(db_column='XSATMT25', max_length=1) 
    satmt25 = models.IntegerField(db_column='SATMT25', blank=True, null=True, verbose_name="sat math 25th percentile score")
    xsatmt75 = models.CharField(db_column='XSATMT75', max_length=1) 
    satmt75 = models.IntegerField(db_column='SATMT75', blank=True, null=True, verbose_name="sat math 75th percentile score")
    xsatwr25 = models.CharField(db_column='XSATWR25', max_length=1) 
    satwr25 = models.IntegerField(db_column='SATWR25', blank=True, null=True, verbose_name="sat writing 25th percentile score")
    xsatwr75 = models.CharField(db_column='XSATWR75', max_length=1) 
    satwr75 = models.IntegerField(db_column='SATWR75', blank=True, null=True, verbose_name="sat writing 75th percentile score")
    xactcm25 = models.CharField(db_column='XACTCM25', max_length=1) 
    actcm25 = models.IntegerField(db_column='ACTCM25', blank=True, null=True, verbose_name="act composite 25th percentile score")
    xactcm75 = models.CharField(db_column='XACTCM75', max_length=1) 
    actcm75 = models.IntegerField(db_column='ACTCM75', blank=True, null=True, verbose_name="act composite 75th percentile score")
    xacten25 = models.CharField(db_column='XACTEN25', max_length=1) 
    acten25 = models.IntegerField(db_column='ACTEN25', blank=True, null=True, verbose_name="act english 25th percentile score")
    xacten75 = models.CharField(db_column='XACTEN75', max_length=1) 
    acten75 = models.IntegerField(db_column='ACTEN75', blank=True, null=True, verbose_name="act english 75th percentile score")
    xactmt25 = models.CharField(db_column='XACTMT25', max_length=1) 
    actmt25 = models.IntegerField(db_column='ACTMT25', blank=True, null=True, verbose_name="act math 25th percentile score")
    xactmt75 = models.CharField(db_column='XACTMT75', max_length=1) 
    actmt75 = models.IntegerField(db_column='ACTMT75', blank=True, null=True, verbose_name="act math 75th percentile score")
    xactwr25 = models.CharField(db_column='XACTWR25', max_length=1) 
    actwr25 = models.IntegerField(db_column='ACTWR25', blank=True, null=True, verbose_name="act writing 25th percentile score")
    xactwr75 = models.CharField(db_column='XACTWR75', max_length=1) 
    actwr75 = models.IntegerField(db_column='ACTWR75', blank=True, null=True, verbose_name="act writing 75th percentile score")
    credits1 = models.IntegerField(db_column='CREDITS1', verbose_name="dual credit")
    credits2 = models.IntegerField(db_column='CREDITS2', verbose_name="credit for life experiences")
    credits3 = models.IntegerField(db_column='CREDITS3', verbose_name="advanced placement (ap) credits")
    credits4 = models.IntegerField(db_column='CREDITS4', verbose_name="institution does not accept dual, credit for life, or ap credits")
    slo5 = models.IntegerField(db_column='SLO5', verbose_name="rotc")
    slo51 = models.IntegerField(db_column='SLO51', verbose_name="rotc - army")
    slo52 = models.IntegerField(db_column='SLO52', verbose_name="rotc - navy")
    slo53 = models.IntegerField(db_column='SLO53', verbose_name="rotc - air force")
    slo6 = models.IntegerField(db_column='SLO6', verbose_name="study abroad")
    slo7 = models.IntegerField(db_column='SLO7', verbose_name="weekend/evening  college")
    slo8 = models.IntegerField(db_column='SLO8', verbose_name="teacher certification (below the postsecondary level)")
    slo81 = models.IntegerField(db_column='SLO81', verbose_name="teacher certification: students can complete their preparation in certain areas of specialization")
    slo82 = models.IntegerField(db_column='SLO82', verbose_name="teacher certification: students must complete their preparation at another institution for certain areas of specialization")
    slo83 = models.IntegerField(db_column='SLO83', verbose_name="teacher certification: approved by the state for initial certifcation or licensure of teachers.")
    slo9 = models.IntegerField(db_column='SLO9', verbose_name="none of the above special learning opportunities are offered")
    yrscoll = models.IntegerField(db_column='YRSCOLL', verbose_name="years of college-level work required")
    stusrv1 = models.IntegerField(db_column='STUSRV1', verbose_name="remedial services")
    stusrv2 = models.IntegerField(db_column='STUSRV2', verbose_name="academic/career counseling service")
    stusrv3 = models.IntegerField(db_column='STUSRV3', verbose_name="employment services for students")
    stusrv4 = models.IntegerField(db_column='STUSRV4', verbose_name="placement services for completers")
    stusrv8 = models.IntegerField(db_column='STUSRV8', verbose_name="on-campus day care for students' children")
    stusrv9 = models.IntegerField(db_column='STUSRV9', verbose_name="none of the above selected services are offered")
    libfac = models.IntegerField(db_column='LIBFAC', verbose_name="library facilities at institution")
    athassoc = models.IntegerField(db_column='ATHASSOC', verbose_name="member of national athletic association")
    assoc1 = models.IntegerField(db_column='ASSOC1', verbose_name="member of national collegiate athletic association (ncaa)")
    assoc2 = models.IntegerField(db_column='ASSOC2', verbose_name="member of national association of intercollegiate athletics (naia)")
    assoc3 = models.IntegerField(db_column='ASSOC3', verbose_name="member of national junior college athletic  association (njcaa)")
    assoc4 = models.IntegerField(db_column='ASSOC4', verbose_name="member of national small college athletic association (nscaa)")
    assoc5 = models.IntegerField(db_column='ASSOC5', verbose_name="member of national christian college athletic association (nccaa)")
    assoc6 = models.IntegerField(db_column='ASSOC6', verbose_name="member of other national athletic association not listed above")
    sport1 = models.IntegerField(db_column='SPORT1', verbose_name="ncaa/naia member for football")
    confno1 = models.IntegerField(db_column='CONFNO1', verbose_name="ncaa/naia conference number football")
    sport2 = models.IntegerField(db_column='SPORT2', verbose_name="ncaa/naia member for basketball")
    confno2 = models.IntegerField(db_column='CONFNO2', verbose_name="ncaa/naia conference number basketball")
    sport3 = models.IntegerField(db_column='SPORT3', verbose_name="ncaa/naia member for baseball")
    confno3 = models.IntegerField(db_column='CONFNO3', verbose_name="ncaa/naia conference number baseball")
    sport4 = models.IntegerField(db_column='SPORT4', verbose_name="ncaa/naia member for cross country/track")
    confno4 = models.IntegerField(db_column='CONFNO4', verbose_name="ncaa/naia conference number cross country/track")
    calsys = models.IntegerField(db_column='CALSYS', verbose_name="calendar system")
    xappfeeu = models.CharField(db_column='XAPPFEEU', max_length=1) 
    applfeeu = models.IntegerField(db_column='APPLFEEU', blank=True, null=True, verbose_name="undergraduate application fee")
    xappfeeg = models.CharField(db_column='XAPPFEEG', max_length=1) 
    applfeeg = models.IntegerField(db_column='APPLFEEG', blank=True, null=True, verbose_name="graduate application fee")
    ft_ug = models.IntegerField(db_column='FT_UG', verbose_name="full-time undergraduate students are enrolled")
    ft_ftug = models.IntegerField(db_column='FT_FTUG', verbose_name="full time first-time degree/certificate-seeking undergraduate students enrolled")
    ftgdnidp = models.IntegerField(db_column='FTGDNIDP', verbose_name="full-time graduate (not including doctor's professional practice) students are enrolled")
    pt_ug = models.IntegerField(db_column='PT_UG', verbose_name="part-time undergraduate students are enrolled")
    pt_ftug = models.IntegerField(db_column='PT_FTUG', verbose_name="part time first-time degree/certificate-seeking undergraduate students enrolled")
    ptgdnidp = models.IntegerField(db_column='PTGDNIDP', verbose_name="part-time graduate (not including doctor's professional practice) students are enrolled")
    docpp = models.IntegerField(db_column='DOCPP', verbose_name="doctor's professional practice students are enrolled")
    docppsp = models.IntegerField(db_column='DOCPPSP', verbose_name="doctor's professional practice students are enrolled in programs formerly designated as first-professional")
    tuitvary = models.IntegerField(db_column='TUITVARY', verbose_name="tuition charge varies for in-district, in-state, out-of-state students")
    room = models.IntegerField(db_column='ROOM', verbose_name="institution provide on-campus housing")
    xroomcap = models.CharField(db_column='XROOMCAP', max_length=1) 
    roomcap = models.IntegerField(db_column='ROOMCAP', blank=True, null=True, verbose_name="total dormitory capacity")
    board = models.IntegerField(db_column='BOARD', verbose_name="institution provides board or meal plan")
    xmealswk = models.CharField(db_column='XMEALSWK', max_length=1) 
    mealswk = models.IntegerField(db_column='MEALSWK', blank=True, null=True, verbose_name="number of meals per week in board charge")
    xroomamt = models.CharField(db_column='XROOMAMT', max_length=1) 
    roomamt = models.IntegerField(db_column='ROOMAMT', blank=True, null=True, verbose_name="typical room charge for academic year")
    xbordamt = models.CharField(db_column='XBORDAMT', max_length=1) 
    boardamt = models.IntegerField(db_column='BOARDAMT', blank=True, null=True, verbose_name="typical board charge for academic year")
    xrmbdamt = models.CharField(db_column='XRMBDAMT', max_length=1) 
    rmbrdamt = models.IntegerField(db_column='RMBRDAMT', blank=True, null=True, verbose_name="combined charge for room and board")
    alloncam = models.IntegerField(db_column='ALLONCAM', verbose_name="full-time, first-time degree/certificate-seeking students required to live on campus")
    xenrlm = models.CharField(db_column='XENRLM', max_length=1) 
    enrlm = models.IntegerField(db_column='ENRLM', blank=True, null=True, verbose_name="enrolled  men")
    xenrlw = models.CharField(db_column='XENRLW', max_length=1) 
    enrlw = models.IntegerField(db_column='ENRLW', blank=True, null=True, verbose_name="enrolled  women")
    xenrlt = models.CharField(db_column='XENRLT', max_length=1) 
    enrlt = models.IntegerField(db_column='ENRLT', blank=True, null=True, verbose_name="enrolled total")
    xapplcn = models.CharField(db_column='XAPPLCN', max_length=1) 
    applcn = models.IntegerField(db_column='APPLCN', blank=True, null=True, verbose_name="applicants total")
    xadmssn = models.CharField(db_column='XADMSSN', max_length=1) 
    admssn = models.IntegerField(db_column='ADMSSN', blank=True, null=True, verbose_name="admissions total")
    xenrlft = models.CharField(db_column='XENRLFT', max_length=1) 
    enrlft = models.IntegerField(db_column='ENRLFT', blank=True, null=True, verbose_name="enrolled full time total")
    xenrlpt = models.CharField(db_column='XENRLPT', max_length=1) 
    enrlpt = models.IntegerField(db_column='ENRLPT', blank=True, null=True, verbose_name="enrolled part time total")
    tuitpl = models.IntegerField(db_column='TUITPL', verbose_name="any alternative tuition plans offered by institution")
    tuitpl1 = models.IntegerField(db_column='TUITPL1', verbose_name="tuition guaranteed plan")
    tuitpl2 = models.IntegerField(db_column='TUITPL2', verbose_name="prepaid tuition plan")
    tuitpl3 = models.IntegerField(db_column='TUITPL3', verbose_name="tuition payment plan")
    tuitpl4 = models.IntegerField(db_column='TUITPL4', verbose_name="other alternative tuition plan")
    disab = models.IntegerField(db_column='DISAB', verbose_name="percent indicator of undergraduates formally registered as students with disabilities")
    xdisabpc = models.CharField(db_column='XDISABPC', max_length=1) 
    disabpct = models.IntegerField(db_column='DISABPCT', blank=True, null=True, verbose_name="percent of undergraduates, who are formally registered as students with disabilities, when percentage is more than 3 percent")
    distnced = models.IntegerField(db_column='DISTNCED', verbose_name="all programs offered completely via distance education")
    dstnced1 = models.IntegerField(db_column='DSTNCED1', verbose_name="undergraduate programs or courses are offered via distance education")
    dstnced2 = models.IntegerField(db_column='DSTNCED2', verbose_name="graduate programs or courses are offered via distance education")
    dstnced3 = models.IntegerField(db_column='DSTNCED3', verbose_name="does not offer distance education opportunities")

    class Meta:
        managed = False
        db_table = 'ic2013'


class TuitionFees(models.Model):
    # student charges for academic year - tuition and fees
    unitid = models.ForeignKey('UnivBaseTable', db_column='UNITID', verbose_name="unique identification number of the institution")
    xtuit1 = models.CharField(db_column='XTUIT1', max_length=1) 
    tuition1 = models.IntegerField(db_column='TUITION1', blank=True, null=True, verbose_name=" in-district average tuition for full-time undergraduates")
    xfee1 = models.CharField(db_column='XFEE1', max_length=1) 
    fee1 = models.IntegerField(db_column='FEE1', blank=True, null=True, verbose_name=" in-district required fees for full-time undergraduates")
    xhrchg1 = models.CharField(db_column='XHRCHG1', max_length=1) 
    hrchg1 = models.IntegerField(db_column='HRCHG1', blank=True, null=True, verbose_name=" in-district per credit hour charge for part-time undergraduates")
    xtuit2 = models.CharField(db_column='XTUIT2', max_length=1) 
    tuition2 = models.IntegerField(db_column='TUITION2', blank=True, null=True, verbose_name="in-state average tuition for full-time undergraduates")
    xfee2 = models.CharField(db_column='XFEE2', max_length=1) 
    fee2 = models.IntegerField(db_column='FEE2', blank=True, null=True, verbose_name="in-state required fees for full-time undergraduates")
    xhrchg2 = models.CharField(db_column='XHRCHG2', max_length=1) 
    hrchg2 = models.IntegerField(db_column='HRCHG2', blank=True, null=True, verbose_name="in-state per credit hour charge for part-time undergraduates")
    xtuit3 = models.CharField(db_column='XTUIT3', max_length=1) 
    tuition3 = models.IntegerField(db_column='TUITION3', blank=True, null=True, verbose_name="out-of-state average tuition for full-time undergraduates")
    xfee3 = models.CharField(db_column='XFEE3', max_length=1) 
    fee3 = models.IntegerField(db_column='FEE3', blank=True, null=True, verbose_name="out-of-state required fees for full-time undergraduates")
    xhrchg3 = models.CharField(db_column='XHRCHG3', max_length=1) 
    hrchg3 = models.IntegerField(db_column='HRCHG3', blank=True, null=True, verbose_name="out-of-state per credit hour charge for part-time undergraduates")
    xtuit5 = models.CharField(db_column='XTUIT5', max_length=1) 
    tuition5 = models.IntegerField(db_column='TUITION5', blank=True, null=True, verbose_name=" in-district average tuition full-time graduates")
    xfee5 = models.CharField(db_column='XFEE5', max_length=1) 
    fee5 = models.IntegerField(db_column='FEE5', blank=True, null=True, verbose_name="in-district required fees for full-time graduates")
    xhrchg5 = models.CharField(db_column='XHRCHG5', max_length=1) 
    hrchg5 = models.IntegerField(db_column='HRCHG5', blank=True, null=True, verbose_name="in-district per credit hour charge part-time graduates")
    xtuit6 = models.CharField(db_column='XTUIT6', max_length=1) 
    tuition6 = models.IntegerField(db_column='TUITION6', blank=True, null=True, verbose_name="in-state average tuition full-time graduates")
    xfee6 = models.CharField(db_column='XFEE6', max_length=1) 
    fee6 = models.IntegerField(db_column='FEE6', blank=True, null=True, verbose_name="in-state required fees for full-time graduates")
    xhrchg6 = models.CharField(db_column='XHRCHG6', max_length=1) 
    hrchg6 = models.IntegerField(db_column='HRCHG6', blank=True, null=True, verbose_name="in-state per credit hour charge part-time graduates")
    xtuit7 = models.CharField(db_column='XTUIT7', max_length=1) 
    tuition7 = models.IntegerField(db_column='TUITION7', blank=True, null=True, verbose_name="out-of-state average tuition full-time graduates")
    xfee7 = models.CharField(db_column='XFEE7', max_length=1) 
    fee7 = models.IntegerField(db_column='FEE7', blank=True, null=True, verbose_name="out-of-state required fees for full-time graduates")
    xhrchg7 = models.CharField(db_column='XHRCHG7', max_length=1) 
    hrchg7 = models.IntegerField(db_column='HRCHG7', blank=True, null=True, verbose_name="out-of-state per credit hour charge part-time graduates")
    xispro1 = models.CharField(db_column='XISPRO1', max_length=1) 
    isprof1 = models.IntegerField(db_column='ISPROF1', blank=True, null=True, verbose_name="chiropractic: in-state tuition")
    xispfe1 = models.CharField(db_column='XISPFE1', max_length=1) 
    ispfee1 = models.IntegerField(db_column='ISPFEE1', blank=True, null=True, verbose_name=" chiropractic: in-state required fees")
    xospro1 = models.CharField(db_column='XOSPRO1', max_length=1) 
    osprof1 = models.IntegerField(db_column='OSPROF1', blank=True, null=True, verbose_name=" chiropractic: out-of-state tuition")
    xospfe1 = models.CharField(db_column='XOSPFE1', max_length=1) 
    ospfee1 = models.IntegerField(db_column='OSPFEE1', blank=True, null=True, verbose_name=" chiropractic: out-of-state required fees")
    xispro2 = models.CharField(db_column='XISPRO2', max_length=1) 
    isprof2 = models.IntegerField(db_column='ISPROF2', blank=True, null=True, verbose_name="dentistry: in-state tuition")
    xispfe2 = models.CharField(db_column='XISPFE2', max_length=1) 
    ispfee2 = models.IntegerField(db_column='ISPFEE2', blank=True, null=True, verbose_name="dentistry: in-state required fees")
    xospro2 = models.CharField(db_column='XOSPRO2', max_length=1) 
    osprof2 = models.IntegerField(db_column='OSPROF2', blank=True, null=True, verbose_name="dentistry: out-of-state tuition")
    xospfe2 = models.CharField(db_column='XOSPFE2', max_length=1) 
    ospfee2 = models.IntegerField(db_column='OSPFEE2', blank=True, null=True, verbose_name="dentistry: out-of-state required fees")
    xispro3 = models.CharField(db_column='XISPRO3', max_length=1) 
    isprof3 = models.IntegerField(db_column='ISPROF3', blank=True, null=True, verbose_name="medicine: in-state tuition")
    xispfe3 = models.CharField(db_column='XISPFE3', max_length=1) 
    ispfee3 = models.IntegerField(db_column='ISPFEE3', blank=True, null=True, verbose_name="medicine: in-state required fees")
    xospro3 = models.CharField(db_column='XOSPRO3', max_length=1) 
    osprof3 = models.IntegerField(db_column='OSPROF3', blank=True, null=True, verbose_name="medicine: out-of-state tuition")
    xospfe3 = models.CharField(db_column='XOSPFE3', max_length=1) 
    ospfee3 = models.IntegerField(db_column='OSPFEE3', blank=True, null=True, verbose_name="medicine: out-of-state required fees")
    xispro4 = models.CharField(db_column='XISPRO4', max_length=1) 
    isprof4 = models.IntegerField(db_column='ISPROF4', blank=True, null=True, verbose_name="optometry: in-state tuition")
    xispfe4 = models.CharField(db_column='XISPFE4', max_length=1) 
    ispfee4 = models.IntegerField(db_column='ISPFEE4', blank=True, null=True, verbose_name="optometry: in-state required fees")
    xospro4 = models.CharField(db_column='XOSPRO4', max_length=1) 
    osprof4 = models.IntegerField(db_column='OSPROF4', blank=True, null=True, verbose_name="optometry: out-of-state tuition")
    xospfe4 = models.CharField(db_column='XOSPFE4', max_length=1) 
    ospfee4 = models.IntegerField(db_column='OSPFEE4', blank=True, null=True, verbose_name="optometry: out-of-state required fees")
    xispro5 = models.CharField(db_column='XISPRO5', max_length=1) 
    isprof5 = models.IntegerField(db_column='ISPROF5', blank=True, null=True, verbose_name="osteopathic medicine: in-state tuition")
    xispfe5 = models.CharField(db_column='XISPFE5', max_length=1) 
    ispfee5 = models.IntegerField(db_column='ISPFEE5', blank=True, null=True, verbose_name="osteopathic medicine: in-state required fees")
    xospro5 = models.CharField(db_column='XOSPRO5', max_length=1) 
    osprof5 = models.IntegerField(db_column='OSPROF5', blank=True, null=True, verbose_name="osteopathic medicine: out-of-state tuition")
    xospfe5 = models.CharField(db_column='XOSPFE5', max_length=1) 
    ospfee5 = models.IntegerField(db_column='OSPFEE5', blank=True, null=True, verbose_name="osteopathic medicine: out-of-state required fees")
    xispro6 = models.CharField(db_column='XISPRO6', max_length=1) 
    isprof6 = models.IntegerField(db_column='ISPROF6', blank=True, null=True, verbose_name="pharmacy: in-state tuition")
    xispfe6 = models.CharField(db_column='XISPFE6', max_length=1) 
    ispfee6 = models.IntegerField(db_column='ISPFEE6', blank=True, null=True, verbose_name="pharmacy: in-state required fees")
    xospro6 = models.CharField(db_column='XOSPRO6', max_length=1) 
    osprof6 = models.IntegerField(db_column='OSPROF6', blank=True, null=True, verbose_name="pharmacy: out-of-state tuition")
    xospfe6 = models.CharField(db_column='XOSPFE6', max_length=1) 
    ospfee6 = models.IntegerField(db_column='OSPFEE6', blank=True, null=True, verbose_name="pharmacy: out-of-state required fees")
    xispro7 = models.CharField(db_column='XISPRO7', max_length=1) 
    isprof7 = models.IntegerField(db_column='ISPROF7', blank=True, null=True, verbose_name="podiatry: in-state tuition")
    xispfe7 = models.CharField(db_column='XISPFE7', max_length=1) 
    ispfee7 = models.IntegerField(db_column='ISPFEE7', blank=True, null=True, verbose_name="podiatry: in-state required fees")
    xospro7 = models.CharField(db_column='XOSPRO7', max_length=1) 
    osprof7 = models.IntegerField(db_column='OSPROF7', blank=True, null=True, verbose_name="podiatry: out-of-state tuition")
    xospfe7 = models.CharField(db_column='XOSPFE7', max_length=1) 
    ospfee7 = models.IntegerField(db_column='OSPFEE7', blank=True, null=True, verbose_name="podiatry: out-of-state required fees")
    xispro8 = models.CharField(db_column='XISPRO8', max_length=1) 
    isprof8 = models.IntegerField(db_column='ISPROF8', blank=True, null=True, verbose_name="veterinary medicine: in-state tuition")
    xispfe8 = models.CharField(db_column='XISPFE8', max_length=1) 
    ispfee8 = models.IntegerField(db_column='ISPFEE8', blank=True, null=True, verbose_name="veterinary medicine: in-state required fees")
    xospro8 = models.CharField(db_column='XOSPRO8', max_length=1) 
    osprof8 = models.IntegerField(db_column='OSPROF8', blank=True, null=True, verbose_name="veterinary medicine: out-of-state tuition")
    xospfe8 = models.CharField(db_column='XOSPFE8', max_length=1) 
    ospfee8 = models.IntegerField(db_column='OSPFEE8', blank=True, null=True, verbose_name="veterinary medicine: out-of-state required fees")
    xispro9 = models.CharField(db_column='XISPRO9', max_length=1) 
    isprof9 = models.IntegerField(db_column='ISPROF9', blank=True, null=True, verbose_name="law: in-state tuition")
    xispfe9 = models.CharField(db_column='XISPFE9', max_length=1) 
    ispfee9 = models.IntegerField(db_column='ISPFEE9', blank=True, null=True, verbose_name="law: in-state required fees")
    xospro9 = models.CharField(db_column='XOSPRO9', max_length=1) 
    osprof9 = models.IntegerField(db_column='OSPROF9', blank=True, null=True, verbose_name="law: out-of-state tuition")
    xospfe9 = models.CharField(db_column='XOSPFE9', max_length=1) 
    ospfee9 = models.IntegerField(db_column='OSPFEE9', blank=True, null=True, verbose_name="law: out-of-state required fees")
    xchg1at0 = models.CharField(db_column='XCHG1AT0', max_length=1) 
    chg1at0 = models.IntegerField(db_column='CHG1AT0', blank=True, null=True, verbose_name="published in-district tuition 2010-11")
    xchg1af0 = models.CharField(db_column='XCHG1AF0', max_length=1) 
    chg1af0 = models.IntegerField(db_column='CHG1AF0', blank=True, null=True, verbose_name="published in-district fees 2010-11")
    xchg1ay0 = models.CharField(db_column='XCHG1AY0', max_length=1) 
    chg1ay0 = models.IntegerField(db_column='CHG1AY0', blank=True, null=True, verbose_name="published in-district tuition and fees 2010-11")
    xchg1at1 = models.CharField(db_column='XCHG1AT1', max_length=1) 
    chg1at1 = models.IntegerField(db_column='CHG1AT1', blank=True, null=True, verbose_name="published in-district tuition 2011-12")
    xchg1af1 = models.CharField(db_column='XCHG1AF1', max_length=1) 
    chg1af1 = models.IntegerField(db_column='CHG1AF1', blank=True, null=True, verbose_name="published in-district fees 2011-12")
    xchg1ay1 = models.CharField(db_column='XCHG1AY1', max_length=1) 
    chg1ay1 = models.IntegerField(db_column='CHG1AY1', blank=True, null=True, verbose_name="published in-district tuition and fees 2011-12")
    xchg1at2 = models.CharField(db_column='XCHG1AT2', max_length=1) 
    chg1at2 = models.IntegerField(db_column='CHG1AT2', blank=True, null=True, verbose_name="published in-district tuition 2012-13")
    xchg1af2 = models.CharField(db_column='XCHG1AF2', max_length=1) 
    chg1af2 = models.IntegerField(db_column='CHG1AF2', blank=True, null=True, verbose_name="published in-district fees 2012-13")
    xchg1ay2 = models.CharField(db_column='XCHG1AY2', max_length=1) 
    chg1ay2 = models.IntegerField(db_column='CHG1AY2', blank=True, null=True, verbose_name="published in-district tuition and fees 2012-13")
    xchg1at3 = models.CharField(db_column='XCHG1AT3', max_length=1) 
    chg1at3 = models.IntegerField(db_column='CHG1AT3', blank=True, null=True, verbose_name="published in-district tuition 2013-14")
    xchg1af3 = models.CharField(db_column='XCHG1AF3', max_length=1) 
    chg1af3 = models.IntegerField(db_column='CHG1AF3', blank=True, null=True, verbose_name="published in-district fees 2013-14")
    xchg1ay3 = models.CharField(db_column='XCHG1AY3', max_length=1) 
    chg1ay3 = models.IntegerField(db_column='CHG1AY3', blank=True, null=True, verbose_name="published in-district tuition and fees 2013-14")
    chg1tgtd = models.IntegerField(db_column='CHG1TGTD', blank=True, null=True, verbose_name="published in-district tuition 2013-14 guaranteed percent increase (if applicable)")
    chg1fgtd = models.IntegerField(db_column='CHG1FGTD', blank=True, null=True, verbose_name="published in-district fees 2013-14 guaranteed percent increase (if applicable)")
    xchg2at0 = models.CharField(db_column='XCHG2AT0', max_length=1) 
    chg2at0 = models.IntegerField(db_column='CHG2AT0', blank=True, null=True, verbose_name="published in-state tuition 2010-11")
    xchg2af0 = models.CharField(db_column='XCHG2AF0', max_length=1) 
    chg2af0 = models.IntegerField(db_column='CHG2AF0', blank=True, null=True, verbose_name="published in-state fees 2010-11")
    xchg2ay0 = models.CharField(db_column='XCHG2AY0', max_length=1) 
    chg2ay0 = models.IntegerField(db_column='CHG2AY0', blank=True, null=True, verbose_name="published in-state tuition and fees 2010-11")
    xchg2at1 = models.CharField(db_column='XCHG2AT1', max_length=1) 
    chg2at1 = models.IntegerField(db_column='CHG2AT1', blank=True, null=True, verbose_name="published in-state tuition 2011-12")
    xchg2af1 = models.CharField(db_column='XCHG2AF1', max_length=1) 
    chg2af1 = models.IntegerField(db_column='CHG2AF1', blank=True, null=True, verbose_name="published in-state fees 2011-12")
    xchg2ay1 = models.CharField(db_column='XCHG2AY1', max_length=1) 
    chg2ay1 = models.IntegerField(db_column='CHG2AY1', blank=True, null=True, verbose_name="published in-state tuition and fees 2011-12")
    xchg2at2 = models.CharField(db_column='XCHG2AT2', max_length=1) 
    chg2at2 = models.IntegerField(db_column='CHG2AT2', blank=True, null=True, verbose_name="published in-state tuition 2012-13")
    xchg2af2 = models.CharField(db_column='XCHG2AF2', max_length=1) 
    chg2af2 = models.IntegerField(db_column='CHG2AF2', blank=True, null=True, verbose_name="published in-state fees 2012-13")
    xchg2ay2 = models.CharField(db_column='XCHG2AY2', max_length=1) 
    chg2ay2 = models.IntegerField(db_column='CHG2AY2', blank=True, null=True, verbose_name="published in-state tuition and fees 2012-13")
    xchg2at3 = models.CharField(db_column='XCHG2AT3', max_length=1) 
    chg2at3 = models.IntegerField(db_column='CHG2AT3', blank=True, null=True, verbose_name="published in-state tuition 2013-14")
    xchg2af3 = models.CharField(db_column='XCHG2AF3', max_length=1) 
    chg2af3 = models.IntegerField(db_column='CHG2AF3', blank=True, null=True, verbose_name="published in-state fees 2013-14")
    xchg2ay3 = models.CharField(db_column='XCHG2AY3', max_length=1) 
    chg2ay3 = models.IntegerField(db_column='CHG2AY3', blank=True, null=True, verbose_name="published in-state tuition and fees 2013-14")
    chg2tgtd = models.IntegerField(db_column='CHG2TGTD', blank=True, null=True, verbose_name="published in-state tuition 2013-14 guaranteed percent increase (if applicable)")
    chg2fgtd = models.IntegerField(db_column='CHG2FGTD', blank=True, null=True, verbose_name="published in-state fees 2013-14 guaranteed percent increase (if applicable)")
    xchg3at0 = models.CharField(db_column='XCHG3AT0', max_length=1) 
    chg3at0 = models.IntegerField(db_column='CHG3AT0', blank=True, null=True, verbose_name="published out-of-state tuition 2010-11")
    xchg3af0 = models.CharField(db_column='XCHG3AF0', max_length=1) 
    chg3af0 = models.IntegerField(db_column='CHG3AF0', blank=True, null=True, verbose_name="published out-of-state fees 2010-11")
    xchg3ay0 = models.CharField(db_column='XCHG3AY0', max_length=1) 
    chg3ay0 = models.IntegerField(db_column='CHG3AY0', blank=True, null=True, verbose_name="published out-of-state tuition and fees 2010-11")
    xchg3at1 = models.CharField(db_column='XCHG3AT1', max_length=1) 
    chg3at1 = models.IntegerField(db_column='CHG3AT1', blank=True, null=True, verbose_name="published out-of-state tuition 2011-12")
    xchg3af1 = models.CharField(db_column='XCHG3AF1', max_length=1) 
    chg3af1 = models.IntegerField(db_column='CHG3AF1', blank=True, null=True, verbose_name="published out-of-state fees 2011-12")
    xchg3ay1 = models.CharField(db_column='XCHG3AY1', max_length=1) 
    chg3ay1 = models.IntegerField(db_column='CHG3AY1', blank=True, null=True, verbose_name="published out-of-state tuition and fees 2011-12")
    xchg3at2 = models.CharField(db_column='XCHG3AT2', max_length=1) 
    chg3at2 = models.IntegerField(db_column='CHG3AT2', blank=True, null=True, verbose_name="published out-of-state tuition 2012-13")
    xchg3af2 = models.CharField(db_column='XCHG3AF2', max_length=1) 
    chg3af2 = models.IntegerField(db_column='CHG3AF2', blank=True, null=True, verbose_name="published out-of-state fees 2012-13")
    xchg3ay2 = models.CharField(db_column='XCHG3AY2', max_length=1) 
    chg3ay2 = models.IntegerField(db_column='CHG3AY2', blank=True, null=True, verbose_name="published out-of-state tuition and fees 2012-13")
    xchg3at3 = models.CharField(db_column='XCHG3AT3', max_length=1) 
    chg3at3 = models.IntegerField(db_column='CHG3AT3', blank=True, null=True, verbose_name="published out-of-state tuition 2013-14")
    xchg3af3 = models.CharField(db_column='XCHG3AF3', max_length=1) 
    chg3af3 = models.IntegerField(db_column='CHG3AF3', blank=True, null=True, verbose_name="published out-of-state fees 2013-14")
    xchg3ay3 = models.CharField(db_column='XCHG3AY3', max_length=1) 
    chg3ay3 = models.IntegerField(db_column='CHG3AY3', blank=True, null=True, verbose_name="published out-of-state tuition and fees 2013-14")
    chg3tgtd = models.IntegerField(db_column='CHG3TGTD', blank=True, null=True, verbose_name="published out-of-state tuition 2013-14 guaranteed percent increase (if applicable)")
    chg3fgtd = models.IntegerField(db_column='CHG3FGTD', blank=True, null=True, verbose_name="published out-of-state fees 2013-14 guaranteed percent increase (if applicable)")
    xchg4ay0 = models.CharField(db_column='XCHG4AY0', max_length=1) 
    chg4ay0 = models.IntegerField(db_column='CHG4AY0', blank=True, null=True, verbose_name="books and supplies 2010-11")
    xchg4ay1 = models.CharField(db_column='XCHG4AY1', max_length=1) 
    chg4ay1 = models.IntegerField(db_column='CHG4AY1', blank=True, null=True, verbose_name="books and supplies 2011-12")
    xchg4ay2 = models.CharField(db_column='XCHG4AY2', max_length=1) 
    chg4ay2 = models.IntegerField(db_column='CHG4AY2', blank=True, null=True, verbose_name="books and supplies 2012-13")
    xchg4ay3 = models.CharField(db_column='XCHG4AY3', max_length=1) 
    chg4ay3 = models.IntegerField(db_column='CHG4AY3', blank=True, null=True, verbose_name="books and supplies 2013-14")
    xchg5ay0 = models.CharField(db_column='XCHG5AY0', max_length=1) 
    chg5ay0 = models.IntegerField(db_column='CHG5AY0', blank=True, null=True, verbose_name="on campus, room and board 2010-11")
    xchg5ay1 = models.CharField(db_column='XCHG5AY1', max_length=1) 
    chg5ay1 = models.IntegerField(db_column='CHG5AY1', blank=True, null=True, verbose_name="on campus, room and board 2011-12")
    xchg5ay2 = models.CharField(db_column='XCHG5AY2', max_length=1) 
    chg5ay2 = models.IntegerField(db_column='CHG5AY2', blank=True, null=True, verbose_name="on campus, room and board 2012-13")
    xchg5ay3 = models.CharField(db_column='XCHG5AY3', max_length=1) 
    chg5ay3 = models.IntegerField(db_column='CHG5AY3', blank=True, null=True, verbose_name="on campus, room and board 2013-14")
    xchg6ay0 = models.CharField(db_column='XCHG6AY0', max_length=1) 
    chg6ay0 = models.IntegerField(db_column='CHG6AY0', blank=True, null=True, verbose_name="on campus, other expenses 2010-11")
    xchg6ay1 = models.CharField(db_column='XCHG6AY1', max_length=1) 
    chg6ay1 = models.IntegerField(db_column='CHG6AY1', blank=True, null=True, verbose_name="on campus, other expenses 2011-12")
    xchg6ay2 = models.CharField(db_column='XCHG6AY2', max_length=1) 
    chg6ay2 = models.IntegerField(db_column='CHG6AY2', blank=True, null=True, verbose_name="on campus, other expenses 2012-13")
    xchg6ay3 = models.CharField(db_column='XCHG6AY3', max_length=1) 
    chg6ay3 = models.IntegerField(db_column='CHG6AY3', blank=True, null=True, verbose_name="on campus, other expenses 2013-14")
    xchg7ay0 = models.CharField(db_column='XCHG7AY0', max_length=1) 
    chg7ay0 = models.IntegerField(db_column='CHG7AY0', blank=True, null=True, verbose_name="off campus (not with family), room and board 2010-11")
    xchg7ay1 = models.CharField(db_column='XCHG7AY1', max_length=1) 
    chg7ay1 = models.IntegerField(db_column='CHG7AY1', blank=True, null=True, verbose_name="off campus (not with family), room and board 2011-12")
    xchg7ay2 = models.CharField(db_column='XCHG7AY2', max_length=1) 
    chg7ay2 = models.IntegerField(db_column='CHG7AY2', blank=True, null=True, verbose_name="off campus (not with family), room and board 2012-13")
    xchg7ay3 = models.CharField(db_column='XCHG7AY3', max_length=1) 
    chg7ay3 = models.IntegerField(db_column='CHG7AY3', blank=True, null=True, verbose_name="off campus (not with family), room and board 2013-14")
    xchg8ay0 = models.CharField(db_column='XCHG8AY0', max_length=1) 
    chg8ay0 = models.IntegerField(db_column='CHG8AY0', blank=True, null=True, verbose_name="off campus (not with family), other expenses 2010-11")
    xchg8ay1 = models.CharField(db_column='XCHG8AY1', max_length=1) 
    chg8ay1 = models.IntegerField(db_column='CHG8AY1', blank=True, null=True, verbose_name="off campus (not with family), other expenses 2011-12")
    xchg8ay2 = models.CharField(db_column='XCHG8AY2', max_length=1) 
    chg8ay2 = models.IntegerField(db_column='CHG8AY2', blank=True, null=True, verbose_name="off campus (not with family), other expenses 2012-13")
    xchg8ay3 = models.CharField(db_column='XCHG8AY3', max_length=1) 
    chg8ay3 = models.IntegerField(db_column='CHG8AY3', blank=True, null=True, verbose_name="off campus (not with family), other expenses 2013-14")
    xchg9ay0 = models.CharField(db_column='XCHG9AY0', max_length=1) 
    chg9ay0 = models.IntegerField(db_column='CHG9AY0', blank=True, null=True, verbose_name="off campus (with family), other expenses 2010-11")
    xchg9ay1 = models.CharField(db_column='XCHG9AY1', max_length=1) 
    chg9ay1 = models.IntegerField(db_column='CHG9AY1', blank=True, null=True, verbose_name="off campus (with family), other expenses 2011-12")
    xchg9ay2 = models.CharField(db_column='XCHG9AY2', max_length=1) 
    chg9ay2 = models.IntegerField(db_column='CHG9AY2', blank=True, null=True, verbose_name="off campus (with family), other expenses 2012-13")
    xchg9ay3 = models.CharField(db_column='XCHG9AY3', max_length=1) 
    chg9ay3_field = models.IntegerField(db_column='CHG9AY3 ', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'ic2013_ay'


class TuitionFeesbyProgram(models.Model):
    # student charges by program - credit hours 
    unitid = models.ForeignKey('UnivBaseTable', db_column='UNITID', verbose_name="unique identification number of the institution")
    prgmofr = models.IntegerField(db_column='PRGMOFR', verbose_name="number of programs offered")
    cipcode1 = models.FloatField(db_column='CIPCODE1', verbose_name="cip code of largest program",choices=CIPCODE_CHOICES)
    xciptui1 = models.CharField(db_column='XCIPTUI1', max_length=1) 
    ciptuit1 = models.IntegerField(db_column='CIPTUIT1', blank=True, null=True, verbose_name="tuition and fees 2013-14 (institutions with no full-time, first-time, undergraduate students)")
    xcipsup1 = models.CharField(db_column='XCIPSUP1', max_length=1) 
    cipsupp1 = models.IntegerField(db_column='CIPSUPP1', blank=True, null=True, verbose_name="books and supplies 2013-14 (institutions with no full-time, first-time, undergraduate students)")
    xciplgt1 = models.CharField(db_column='XCIPLGT1', max_length=1) 
    ciplgth1 = models.IntegerField(db_column='CIPLGTH1', verbose_name="total length of largest program")
    prgmsr1 = models.IntegerField(db_column='PRGMSR1', verbose_name="largest program measured in credit or contact hours")
    xmthcmp1 = models.CharField(db_column='XMTHCMP1', max_length=1) 
    mthcmp1 = models.IntegerField(db_column='MTHCMP1', verbose_name="average number of months to complete largest program")
    xwkcmp1 = models.CharField(db_column='XWKCMP1', max_length=1) 
    wkcmp1 = models.IntegerField(db_column='WKCMP1', blank=True, null=True, verbose_name="total length of program in weeks, as completed by a student attending full-time")
    xlnayhr1 = models.CharField(db_column='XLNAYHR1', max_length=1) 
    lnayhr1 = models.IntegerField(db_column='LNAYHR1', blank=True, null=True, verbose_name="total length of academic year (as used to calculate your pell budget) in contact or credit hours")
    xlnaywk1 = models.CharField(db_column='XLNAYWK1', max_length=1) 
    lnaywk1 = models.IntegerField(db_column='LNAYWK1', blank=True, null=True, verbose_name="total length of academic year (as used to calculate your pell budget) in weeks")
    xchg1py0 = models.CharField(db_column='XCHG1PY0', max_length=1) 
    chg1py0 = models.IntegerField(db_column='CHG1PY0', blank=True, null=True, verbose_name="published tuition and fees 2010-11")
    xchg1py1 = models.CharField(db_column='XCHG1PY1', max_length=1) 
    chg1py1 = models.IntegerField(db_column='CHG1PY1', blank=True, null=True, verbose_name="published tuition and fees 2011-12")
    xchg1py2 = models.CharField(db_column='XCHG1PY2', max_length=1) 
    chg1py2 = models.IntegerField(db_column='CHG1PY2', blank=True, null=True, verbose_name="published tuition and fees 2012-13")
    xchg1py3 = models.CharField(db_column='XCHG1PY3', max_length=1) 
    chg1py3 = models.IntegerField(db_column='CHG1PY3', blank=True, null=True, verbose_name="published tuition and fees 2013-14")
    xchg4py0 = models.CharField(db_column='XCHG4PY0', max_length=1) 
    chg4py0 = models.IntegerField(db_column='CHG4PY0', blank=True, null=True, verbose_name="books and supplies 2010-11")
    xchg4py1 = models.CharField(db_column='XCHG4PY1', max_length=1) 
    chg4py1 = models.IntegerField(db_column='CHG4PY1', blank=True, null=True, verbose_name="books and supplies 2011-12")
    xchg4py2 = models.CharField(db_column='XCHG4PY2', max_length=1) 
    chg4py2 = models.IntegerField(db_column='CHG4PY2', blank=True, null=True, verbose_name="books and supplies 2012-13")
    xchg4py3 = models.CharField(db_column='XCHG4PY3', max_length=1) 
    chg4py3 = models.IntegerField(db_column='CHG4PY3', blank=True, null=True, verbose_name="books and supplies 2013-14")
    xchg5py0 = models.CharField(db_column='XCHG5PY0', max_length=1) 
    chg5py0 = models.IntegerField(db_column='CHG5PY0', blank=True, null=True, verbose_name="on campus, room and board 2010-11")
    xchg5py1 = models.CharField(db_column='XCHG5PY1', max_length=1) 
    chg5py1 = models.IntegerField(db_column='CHG5PY1', blank=True, null=True, verbose_name="on campus, room and board 2011-12")
    xchg5py2 = models.CharField(db_column='XCHG5PY2', max_length=1) 
    chg5py2 = models.IntegerField(db_column='CHG5PY2', blank=True, null=True, verbose_name="on campus, room and board 2012-13")
    xchg5py3 = models.CharField(db_column='XCHG5PY3', max_length=1) 
    chg5py3 = models.IntegerField(db_column='CHG5PY3', blank=True, null=True, verbose_name="on campus, room and board 2013-14")
    xchg6py0 = models.CharField(db_column='XCHG6PY0', max_length=1) 
    chg6py0 = models.IntegerField(db_column='CHG6PY0', blank=True, null=True, verbose_name="on campus, other expenses 2010-11")
    xchg6py1 = models.CharField(db_column='XCHG6PY1', max_length=1) 
    chg6py1 = models.IntegerField(db_column='CHG6PY1', blank=True, null=True, verbose_name="on campus, other expenses 2011-12")
    xchg6py2 = models.CharField(db_column='XCHG6PY2', max_length=1) 
    chg6py2 = models.IntegerField(db_column='CHG6PY2', blank=True, null=True, verbose_name="on campus, other expenses 2012-13")
    xchg6py3 = models.CharField(db_column='XCHG6PY3', max_length=1) 
    chg6py3 = models.IntegerField(db_column='CHG6PY3', blank=True, null=True, verbose_name="on campus, other expenses 2013-14")
    xchg7py0 = models.CharField(db_column='XCHG7PY0', max_length=1) 
    chg7py0 = models.IntegerField(db_column='CHG7PY0', blank=True, null=True, verbose_name="off campus (not with family), room and board 2010-11")
    xchg7py1 = models.CharField(db_column='XCHG7PY1', max_length=1) 
    chg7py1 = models.IntegerField(db_column='CHG7PY1', blank=True, null=True, verbose_name="off campus (not with family), room and board 2011-12")
    xchg7py2 = models.CharField(db_column='XCHG7PY2', max_length=1) 
    chg7py2 = models.IntegerField(db_column='CHG7PY2', blank=True, null=True, verbose_name="off campus (not with family), room and board 2012-13")
    xchg7py3 = models.CharField(db_column='XCHG7PY3', max_length=1) 
    chg7py3 = models.IntegerField(db_column='CHG7PY3', blank=True, null=True, verbose_name="off campus (not with family), room and board 2013-14")
    xchg8py0 = models.CharField(db_column='XCHG8PY0', max_length=1) 
    chg8py0 = models.IntegerField(db_column='CHG8PY0', blank=True, null=True, verbose_name="off campus (not with family), other expenses 2010-11")
    xchg8py1 = models.CharField(db_column='XCHG8PY1', max_length=1) 
    chg8py1 = models.IntegerField(db_column='CHG8PY1', blank=True, null=True, verbose_name="off campus (not with family), other expenses 2011-12")
    xchg8py2 = models.CharField(db_column='XCHG8PY2', max_length=1) 
    chg8py2 = models.IntegerField(db_column='CHG8PY2', blank=True, null=True, verbose_name="off campus (not with family), other expenses 2012-13")
    xchg8py3 = models.CharField(db_column='XCHG8PY3', max_length=1) 
    chg8py3 = models.IntegerField(db_column='CHG8PY3', blank=True, null=True, verbose_name="off campus (not with family), other expenses 2013-14")
    xchg9py0 = models.CharField(db_column='XCHG9PY0', max_length=1) 
    chg9py0 = models.IntegerField(db_column='CHG9PY0', blank=True, null=True, verbose_name="off campus (with family), other expenses 2010-11")
    xchg9py1 = models.CharField(db_column='XCHG9PY1', max_length=1) 
    chg9py1 = models.IntegerField(db_column='CHG9PY1', blank=True, null=True, verbose_name="off campus (with family), other expenses 2011-12")
    xchg9py2 = models.CharField(db_column='XCHG9PY2', max_length=1) 
    chg9py2 = models.IntegerField(db_column='CHG9PY2', blank=True, null=True, verbose_name="off campus (with family), other expenses 2012-13")
    xchg9py3 = models.CharField(db_column='XCHG9PY3', max_length=1) 
    chg9py3 = models.IntegerField(db_column='CHG9PY3', blank=True, null=True, verbose_name="off campus (with family), other expenses 2013-14")
    cipcode2 = models.FloatField(db_column='CIPCODE2', verbose_name="cip code of 2nd largest program",choices=CIPCODE_CHOICES)
    xciptui2 = models.CharField(db_column='XCIPTUI2', max_length=1) 
    ciptuit2 = models.IntegerField(db_column='CIPTUIT2', blank=True, null=True, verbose_name="tuition and fees of 2nd largest program")
    xcipsup2 = models.CharField(db_column='XCIPSUP2', max_length=1) 
    cipsupp2 = models.IntegerField(db_column='CIPSUPP2', blank=True, null=True, verbose_name="cost of books and supplies of 2nd largest program")
    xciplgt2 = models.CharField(db_column='XCIPLGT2', max_length=1) 
    ciplgth2 = models.IntegerField(db_column='CIPLGTH2', blank=True, null=True, verbose_name="length of 2nd largest program")
    prgmsr2 = models.IntegerField(db_column='PRGMSR2', verbose_name="2nd largest program measured in credit or contact hours")
    xmthcmp2 = models.CharField(db_column='XMTHCMP2', max_length=1) 
    mthcmp2 = models.IntegerField(db_column='MTHCMP2', blank=True, null=True, verbose_name="number of months to complete 2nd largest program")
    cipcode3 = models.FloatField(db_column='CIPCODE3', verbose_name="cip code of 3rd largest program",choices=CIPCODE_CHOICES)
    xciptui3 = models.CharField(db_column='XCIPTUI3', max_length=1) 
    ciptuit3 = models.IntegerField(db_column='CIPTUIT3', blank=True, null=True, verbose_name="tuition and fees of 3rd largest program")
    xcipsup3 = models.CharField(db_column='XCIPSUP3', max_length=1) 
    cipsupp3 = models.IntegerField(db_column='CIPSUPP3', blank=True, null=True, verbose_name="cost of books and supplies of 3rd largest program")
    xciplgt3 = models.CharField(db_column='XCIPLGT3', max_length=1) 
    ciplgth3 = models.IntegerField(db_column='CIPLGTH3', blank=True, null=True, verbose_name="length of 3rd largest program")
    prgmsr3 = models.IntegerField(db_column='PRGMSR3', verbose_name="3rd largest program measured in credit or contact hours")
    xmthcmp3 = models.CharField(db_column='XMTHCMP3', max_length=1) 
    mthcmp3 = models.IntegerField(db_column='MTHCMP3', blank=True, null=True, verbose_name="number of months to complete 3rd largest program")
    cipcode4 = models.FloatField(db_column='CIPCODE4', verbose_name="cip code of 4th largest program",choices=CIPCODE_CHOICES)
    xciptui4 = models.CharField(db_column='XCIPTUI4', max_length=1) 
    ciptuit4 = models.IntegerField(db_column='CIPTUIT4', blank=True, null=True, verbose_name="tuition and fees of 4th largest program")
    xcipsup4 = models.CharField(db_column='XCIPSUP4', max_length=1) 
    cipsupp4 = models.IntegerField(db_column='CIPSUPP4', blank=True, null=True, verbose_name="cost of books and supplies of 4th largest program")
    xciplgt4 = models.CharField(db_column='XCIPLGT4', max_length=1) 
    ciplgth4 = models.IntegerField(db_column='CIPLGTH4', blank=True, null=True, verbose_name="length of 4th largest program")
    prgmsr4 = models.IntegerField(db_column='PRGMSR4', verbose_name="4th largest program measured in credit or contact hours")
    xmthcmp4 = models.CharField(db_column='XMTHCMP4', max_length=1) 
    mthcmp4 = models.IntegerField(db_column='MTHCMP4', blank=True, null=True, verbose_name="number of months to complete 4th largest program")
    cipcode5 = models.FloatField(db_column='CIPCODE5', verbose_name="cip code of 5th largest program",choices=CIPCODE_CHOICES)
    xciptui5 = models.CharField(db_column='XCIPTUI5', max_length=1) 
    ciptuit5 = models.IntegerField(db_column='CIPTUIT5', blank=True, null=True, verbose_name="tuition and fees of 5th largest program")
    xcipsup5 = models.CharField(db_column='XCIPSUP5', max_length=1) 
    cipsupp5 = models.IntegerField(db_column='CIPSUPP5', blank=True, null=True, verbose_name="cost of books and supplies of 5th largest program")
    xciplgt5 = models.CharField(db_column='XCIPLGT5', max_length=1) 
    ciplgth5 = models.IntegerField(db_column='CIPLGTH5', blank=True, null=True, verbose_name="length of 5th largest program")
    prgmsr5 = models.IntegerField(db_column='PRGMSR5', verbose_name="5th largest program measured in credit or contact hours")
    xmthcmp5 = models.CharField(db_column='XMTHCMP5', max_length=1) 
    mthcmp5 = models.IntegerField(db_column='MTHCMP5', blank=True, null=True, verbose_name="number of months to complete 5th largest program")
    cipcode6 = models.FloatField(db_column='CIPCODE6', verbose_name="cip code of 6th largest program",choices=CIPCODE_CHOICES)
    xciptui6 = models.CharField(db_column='XCIPTUI6', max_length=1) 
    ciptuit6 = models.IntegerField(db_column='CIPTUIT6', blank=True, null=True, verbose_name="tuition and fees of 6th largest program")
    xcipsup6 = models.CharField(db_column='XCIPSUP6', max_length=1) 
    cipsupp6 = models.IntegerField(db_column='CIPSUPP6', blank=True, null=True, verbose_name="cost of books and supplies of 6th largest program")
    xciplgt6 = models.CharField(db_column='XCIPLGT6', max_length=1) 
    ciplgth6 = models.IntegerField(db_column='CIPLGTH6', blank=True, null=True, verbose_name="length of 6th largest program")
    prgmsr6 = models.IntegerField(db_column='PRGMSR6', verbose_name="6th largest program measured in credit or contact hours")
    xmthcmp6 = models.CharField(db_column='XMTHCMP6', max_length=1) 
    mthcmp6_field = models.IntegerField(db_column='MTHCMP6 ', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'ic2013_py'


class USNWR(models.Model):
    rank = models.IntegerField(db_column='RANK')
    name = models.CharField(db_column='NAME', max_length=500)
    unitid = models.OneToOneField('UnivBaseTable', db_column='UNITID', related_name='rank')

    class Meta:
        managed = False
        db_table = 'usnwr_rankings'
        ordering = ['rank']

class AppFlowRate(models.Model):
    unitid = models.OneToOneField('UnivBaseTable', db_column='UNITID', related_name='app_flow_rates')
    app_on = models.DecimalField(db_column="APPONS", decimal_places=10, max_digits=10)
    app_off = models.DecimalField(db_column="APPOFS", decimal_places=10, max_digits=10)
    qual_on = models.DecimalField(db_column="QUALONS", decimal_places=10, max_digits=10)
    qual_off = models.DecimalField(db_column="QUALOFS", decimal_places=10, max_digits=10)
    bqual_on = models.DecimalField(db_column="BQUALONS", decimal_places=10, max_digits=10)
    bqual_off = models.DecimalField(db_column="BQUALOFS", decimal_places=10, max_digits=10)
    hire_on = models.DecimalField(db_column="HIREONS", decimal_places=10, max_digits=10)
    hire_off = models.DecimalField(db_column="HIREOFS", decimal_places=10, max_digits=10)

    class Meta:
        managed = False
        db_table = 'sch_tbl_rates'
