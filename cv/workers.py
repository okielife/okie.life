import json

from .models import Publication, Education, Person, Experience, Skill, MembershipItem, ProjectAttribute


def json_to_string(obj):
    return json.dumps(obj)


def get_all():
    ret_dict = dict()
    ret_dict['degrees'] = get_education()
    ret_dict['pubs'] = get_publications()
    ret_dict['person'] = get_person()
    ret_dict['experiences'] = get_experience()
    ret_dict['skills'] = get_skills()
    ret_dict['memberships'] = get_memberships()
    ret_dict['projects'] = get_projects()
    return ret_dict


def get_person():
    person = Person()
    person.name = "Edwin Lee"
    person.email = "leeed2001@gmail.com"
    person.github_id = "myoldmopar"
    person.goal = "My goal is to leverage my skills as a programmer, mechanical engineer, and numerical analyst in the field of advanced building and system simulation."
    return person


def get_education():
    degrees = list()
    degrees.append(Education(
        degree="Doctor of Philosophy",
        field="Mechanical Engineering",
        school="Oklahoma State University",
        date="May 2013",
        thesis="A Generalized Pipe Heat Transfer Model for Whole Building Simulation Applications",
        gpa=4.0,
    ))
    degrees.append(Education(
        degree="Master of Science",
        field="Mechanical Engineering",
        school="Oklahoma State University",
        date="May 2008",
        thesis="Development, Implementation, and Verification of a Buried Pipe Model in EnergyPlus",
        gpa=4.0,
    ))
    degrees.append(Education(
        degree="Bachelor of Science",
        field="Mechanical Engineering",
        school="Oklahoma State University",
        date="May 2006",
        gpa=3.52,
    ))
    return degrees


def get_publications():
    pubs = list()
    pubs.append(Publication(
        authors="Raftery, P., E. Lee, T. Webster, T. Hoyt and F. Bauman",
        year=2014,
        title="Effects of furniture and contents on peak cooling load",
        container="Energy and Buildings: 85:445-457"
    ))
    pubs.append(Publication(
        authors="Studer, D., K. Fleming, E. Lee and W. Livingood",
        year=2014,
        title="Enabling Detailed Energy Analyses via the Technology Performance Exchange",
        container="Proceedings of the ACEEE Summer Study, Pacific Grove, CA, USA"
    ))
    pubs.append(Publication(
        authors="Lee, E., D. Fisher and J. Spitler",
        year=2013,
        title="Efficient Horizontal Ground Heat Exchanger Simulation with Zone Heat Balance Integration",
        container="HVAC&R Research: 19(3):307-323"
    ))
    pubs.append(Publication(
        authors="Lee, E. and D. Studer",
        year=2013,
        title="TIP 287: Reducing Technology Evaluation Costs Through a Technology Performance Exchange. Deliverable 2.5: Draft Data Entry Forms",
        container="NREL Report No. TP-5500-60219"
    ))
    pubs.append(Publication(
        authors="Xiong, Z., E. Lee and D. Fisher",
        year=2013,
        title="Development of a Horizontal Slinky Ground Heat Exchanger Model",
        container="ASHRAE Transactions: 119(2)"
    ))
    pubs.append(Publication(
        authors="Chandrasekharan, R., E. Lee, D. Fisher and P. Deokar",
        year=2013,
        title="An Enhanced Simulation Model for Building Envelopes with Phase Change Materials",
        container="ASHRAE Transactions: 119(2)"
    ))
    pubs.append(Publication(
        authors="Cullin, J., Spitler, J. and E. Lee",
        year=2013,
        title="Preliminary Investigation of the Effect of Horizontal Piping on the Performance of a Vertical Ground Heat Exchanger System",
        container="ASHRAE Transactions: 119(2):302-311"
    ))
    pubs.append(Publication(
        authors="Webster, T., T. Hoyt, E. Lee, A. Daly, D. Feng, F. Bauman, S. Schiavon, K. Ho Lee, W. Pasut and D. Fisher",
        year=2012,
        title="Influence of Design and Operating Conditions on Underfloor Air Distribution (UFAD) System Performance",
        container="Proceedings of Simbuild 2012, August 1-3, Madison, Wisconsin"
    ))
    pubs.append(Publication(
        authors="Cullin, J.R., L. Xing, E. Lee, J.D. Spitler and D.E. Fisher",
        year=2012,
        title="Feasibility of Foundation Heat Exchangers In Ground Source Heat Pump Systems In the United States",
        container="ASHRAE Transactions: 118(1):1039-1048"
    ))
    pubs.append(Publication(
        authors="Kony, J., D. Yarbrough, W. Miller, P. Childs, J. Atchley, S. Shrestha, E. Kossecka, J. B. Smith, T. Fellinger, E. Lee, and M. Bianchi",
        year=2010,
        title="Theoretical and Experimental Thermal Performance Analysis of Building Shell Components Containing Blown Fiberglass Insulation Enhanced with Phase Change Material (PCM)",
        container=" Proceedings of ASHRAE THERM XII, Clearwater, FL"
    ))
    pubs.append(Publication(
        authors="Spitler, J., J. Cullin, M. Bernier, M. Kummert, P. Cui, X. Liu, E. Lee, and D. Fisher",
        year=2009,
        title="Preliminary intermodel comparison of ground heat exchanger simulation models",
        container="Proceedings of 11th International Conference on Thermal Energy Storage; Effstock 2009, Stockholm, Sweden"
    ))
    pubs.append(Publication(
        authors="Cremaschi, L.,and E. Lee",
        year=2008,
        title="Design and Heat Transfer Analysis of a New Psychrometric Environmental Chamber for Heat Pump and Refrigeration Systems Testing",
        container="ASHRAE Transactions 114(2):619-631"
    ))
    return pubs


def get_experience():
    jobs = list()
    e = Experience(
        title="Research Engineer, Multi-disciplinary",
        date="May 2013 - Present",
        company="National Renewable Energy Laboratory, Golden, CO",
    )
    e.json_blob = [
        "Contributed to the Technology Performance Exchange, adding data entry forms for multiple technologies",
        "Created the translator that converts TPEx datasets into components on the Building Component Library",
        "Began leading technical development of EnergyPlus",
        "Overseeing the technical changes accompanying the translation from FORTRAN to C++, and StarTeam to GitHub"
    ]
    jobs.append(e)

    e = Experience(
        title="Graduate Research Assistant",
        date="January 2006 - May 2013",
        company="Oklahoma State University, Stillwater, OK",
    )
    e.json_blob = [
        "Designer of many aspects of the updated EnergyPlus central plant simulation",
        "Developed a generalized horizontal ground heat exchanger model that includes zone thermal interaction",
        "Performed experimental measurement and modeling of transport delay phenomena in piping systems",
        "Provided simulation support for UFAD and internal mass cases to the Center for the Built Environment"
    ]
    jobs.append(e)

    e = Experience(
        title="Engineering Consultant",
        date="Fall 2007, Summer 2009",
        company="Oak Ridge National Laboratory, Oak Ridge, TN",
    )
    e.json_blob = [
        "Performed EnergyPlus simulations and analysis investigating building envelopes, including PCMs"
    ]
    jobs.append(e)

    e = Experience(
        title="Engineering Intern",
        date="Summer 2005",
        company="Specific Systems, Tulsa, OK",
    )
    e.json_blob = [
        "Learned and assisted with design and manufacturing of modular HVAC equipment",
        "Designed and fabricated parts.",
        "Performed various mechanical and structural analysis on designs.",
        "Aided in the construction of a thermal test chamber."
    ]
    jobs.append(e)
    return jobs


def get_skills():
    skills = dict()
    these_skills = list()
    these_skills.append(Skill(
        description="Proficient with Windows, Mac, and Linux (multiple distributions) Operating System Environments",
    ))
    skills["General Computing"] = these_skills
    these_skills = list()
    these_skills.append(Skill(
        description='Scripting Languages: Batch (Windows), Bash (Linux), Python, Ruby',
    ))
    these_skills.append(Skill(
        description='Programming Languages: FORTRAN, C, C++, Python, VB.Net, VBA, Modelica, (Including Language Interop)',
    ))
    these_skills.append(Skill(
        description='GUI Development: VB.Net (Windows), Python (Cross-platform)',
    ))
    these_skills.append(Skill(
        description='Software version control tools, including Borland Starteam, Git, Subversion, and Bazaar',
    ))
    skills["Software Development"] = these_skills
    these_skills = list()
    these_skills.append(Skill(
        description='Publication tools, including LaTeX and GnuPlot',
    ))
    these_skills.append(Skill(
        description='Office suites, including LibreOffice and MS Office, Gnumeric',
    ))
    these_skills.append(Skill(
        description='Publication tools, including LaTeX and GnuPlot',
    ))
    these_skills.append(Skill(
        description='Software Tools, including EES, MathCAD, R, Fluent, AutoCAD, LibreCAD and Octave (Matlab)',
    ))
    these_skills.append(Skill(
        description='Virtual machine utilization',
    ))
    these_skills.append(Skill(
        description='Web Development using Django',
    ))
    skills["Other Software"] = these_skills
    return skills


def get_memberships():
    memberships = dict()
    this_membership = list()
    this_membership.append(MembershipItem(
        description="Student Member 2005-2013"
    ))
    this_membership.append(MembershipItem(
        description="Student Branch President 2007-2012"
    ))
    this_membership.append(MembershipItem(
        description="Member 2013-Present"
    ))
    memberships["American Society of Heating, Refrigerating, and Air-Conditioning Engineers"] = this_membership
    this_membership = list()
    this_membership.append(MembershipItem(
        description="Phi Kappa Phi Honor Society: Superior Scholarship"
    ))
    this_membership.append(MembershipItem(
        description="A. B. Still Memorial Scholarship: Performance in Mechanical Engineering"
    ))
    this_membership.append(MembershipItem(
        description="Two-time ASHRAE Memorial Scholarship: Performance and Research Interests"
    ))
    this_membership.append(MembershipItem(
        description="Conoco-Phillips Memorial Scholarship: Performance in Graduate Studies"
    ))
    this_membership.append(MembershipItem(
        description="Central Oklahoma ASHRAE Chapter Graduate Fellowship: Performance in Graduate Studies"
    ))
    memberships["Honors"] = this_membership
    return memberships


def get_projects():
    projects = dict()
    this_project = list()
    this_project.append(ProjectAttribute(
        description="Generalized buried pipe heat transfer model",
    ))
    this_project.append(ProjectAttribute(
        description="Plant pressure algorithms",
    ))
    this_project.append(ProjectAttribute(
        description="Central plant solver overhaul",
    ))
    this_project.append(ProjectAttribute(
        description="Development of a new testing framework",
    ))
    this_project.append(ProjectAttribute(
        description="Overseeing technical efforts for Fortran to C++ translation and StarTeam to GitHub transition",
    ))
    projects["EnergyPlus"] = this_project
    this_project = list()
    this_project.append(ProjectAttribute(
        description="A graphical tool to improve work-flow during development of EnergyPlus",
    ))
    this_project.append(ProjectAttribute(
        description="Ability to modify reporting frequency/contents to any idf without opening the file",
    ))
    this_project.append(ProjectAttribute(
        description="Test suite tool to provide specific testing of particular file types and configurations",
    ))
    this_project.append(ProjectAttribute(
        description="Parametric tool using the EPMacro preprocessor, allows a generic number of parameters",
    ))
    this_project.append(ProjectAttribute(
        description="Direct access to calculate a mathematical difference summary of two EnergyPlus output files",
    ))
    this_project.append(ProjectAttribute(
        description="An IDF analyzer that compares directories of IDFs",
    ))
    this_project.append(ProjectAttribute(
        description="Ability to run an EnergyPlus simulation on any input file with a single click using a compiled EnergyPlus library",
    ))
    projects["EnergyPlus Focus"] = this_project
    this_project = list()
    this_project.append(ProjectAttribute(
        description="A tool to regress manufacturer's data into EnergyPlus inputs",
    ))
    this_project.append(ProjectAttribute(
        description="Ability to paste in tabulated and correction factor data",
    ))
    this_project.append(ProjectAttribute(
        description="Creates a graphical report showing the resulting parameter quality",
    ))
    this_project.append(ProjectAttribute(
        description="Modular code allows for easy extension for new model types",
    ))
    this_project.append(ProjectAttribute(
        description="Multithreaded code allows the graphical interface to run while background operations perform the curve fit or parameter estimation",
    ))
    projects["Plant Parameter Estimation"] = this_project
    this_project = list()
    this_project.append(ProjectAttribute(
        description="A graphical tool for performing buried pipe simulations",
    ))
    this_project.append(ProjectAttribute(
        description="Formal XML input/output program structure",
    ))
    this_project.append(ProjectAttribute(
        description="Utilizes the same model that is implemented in EnergyPlus for buried pipe simulations",
    ))
    this_project.append(ProjectAttribute(
        description="Graphical mesh display and temperature/thermal property distribution",
    ))
    projects["Buried Pipe Heat Transfer Tool"] = this_project
    this_project = list()
    this_project.append(ProjectAttribute(
        description="A graphical Python application for monitoring data acquisition",
    ))
    this_project.append(ProjectAttribute(
        description="Monitors data acquisition from a serial/USB port RS-232 device",
    ))
    this_project.append(ProjectAttribute(
        description="Records raw data signals, converts to an analog, and processes into physical measurements where applicable",
    ))
    this_project.append(ProjectAttribute(
        description="Running graphs on-screen show each measurement status",
    ))
    this_project.append(ProjectAttribute(
        description="Implemented on a Linux machine, portable to other operating systems",
    ))
    projects["Data Acquisition"] = this_project
    this_project = list()
    this_project.append(ProjectAttribute(
        description="Multi-language library for accessing/manipulating idd and idf files",
    ))
    this_project.append(ProjectAttribute(
        description="VB.Net based library parses IDD and IDF with extensive error handling",
    ))
    this_project.append(ProjectAttribute(
        description="VB.Net application includes GUI and file comparison tools",
    ))
    this_project.append(ProjectAttribute(
        description="Python cross platform library is lightweight, simple, with minimal error handling",
    ))
    this_project.append(ProjectAttribute(
        description="Python application allows quick processing of well-formed idfs including multiple file comparisons",
    ))
    projects["IDD/IDF Library"] = this_project
    return projects
