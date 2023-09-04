from flask import Flask, render_template, jsonify, request
import numpy as np
import joblib

X = ["bed", "bath", "house_size", "city_aberdeen", "city_abington", "city_absecon", "city_acton", "city_acushnet", "city_adams", "city_addisleigh park", "city_agawam", "city_airmont", "city_albertson", "city_alexandria township", "city_alford", "city_allamuchy township", "city_allendale", "city_allentown", "city_allenwood", "city_alloway", "city_alpha", "city_amawalk", "city_amenia", "city_amesbury", "city_amherst", "city_ancram", "city_andover", "city_ardsley", "city_argyle", "city_arlington", "city_armonk", "city_arverne", "city_asbury park", "city_ashburnham", "city_ashby", "city_ashfield", "city_ashland", "city_astoria", "city_atco", "city_athol", "city_atlantic city", "city_atlantic highlands", "city_attleboro", "city_auburn", "city_audubon", "city_austerlitz", "city_avalon", "city_avalon manor", "city_avenel", "city_avon by the sea", "city_ayer", "city_bardonia", "city_barnegat", "city_barnegat light", "city_barnegat township", "city_barnstable", "city_barre", "city_barrington", "city_barryville", "city_bay head", "city_bayonne", "city_bayside", "city_bayville", "city_beach haven", "city_beach haven west", "city_beachwood", "city_becket", "city_bed stuy", "city_bedford", "city_bedminster twp", "city_beechhurst", "city_belchertown", "city_belford", "city_belle harbor", "city_belle mead", "city_belle terre", "city_belleplain", "city_bellerose", "city_belleville", "city_bellingham", "city_bellmawr", "city_belmar", "city_belmont", "city_belvidere", "city_berkeley", "city_berkeley heights twp", "city_berkley", "city_berlin", "city_bernards twp", "city_bernardston", "city_bernardsville", "city_bethlehem township", "city_beverly", "city_billerica", "city_blackstone", "city_blackwood", "city_blairstown", "city_blandford", "city_blauvelt", "city_bloomfield", "city_blooming grove", "city_bloomingdale", "city_bloomsbury", "city_blue anchor", "city_bolton", "city_boonton", "city_boonton township", "city_bordentown", "city_boston", "city_bound brook", "city_bourne", "city_boxborough", "city_boxford", "city_boylston", "city_bradley beach", "city_braintree", "city_branchburg", "city_branchburg township", "city_branchville", "city_brewster", "city_briarcliff manor", "city_briarwood", "city_brick", "city_bridgeton", "city_bridgewater", "city_bridgewater twp", "city_brielle", "city_brigantine", "city_brigantine city", "city_brighton", "city_brimfield", "city_broad channel", "city_brockton", "city_bronx", "city_bronxville", "city_brooklawn", "city_brookline", "city_brooklyn", "city_browns mills", "city_brownville", "city_buckland", "city_buena vista township", "city_burlington", "city_burlington township", "city_butler", "city_buzzards bay", "city_byram township", "city_caldwell boro township", "city_califon", "city_cambria heights", "city_cambridge", "city_cambridge village", "city_camden", "city_canaan", "city_canton", "city_cape may", "city_cape may beach", "city_cape may court house", "city_cape may point", "city_carlisle", "city_carlstadt", "city_carmel", "city_carneys point", "city_carteret", "city_carver", "city_cataumet", "city_cedar grove", "city_cedarhurst", "city_cedarville", "city_centereach", "city_centerville", "city_central valley", "city_champlain", "city_chappaqua", "city_charlestown", "city_charlton", "city_chatham", "city_chatham township", "city_chatham village", "city_chatsworth", "city_chazy", "city_chelmsford", "city_chelsea", "city_cherry hill", "city_cheshire", "city_chester", "city_chester township", "city_chesterfield", "city_chestnut ridge", "city_chicopee", "city_cinnaminson", "city_city of orange township", "city_clark", "city_clarksboro", "city_clarksburg", "city_claverack", "city_clayton", "city_clementon", "city_clermont", "city_cliffside park", "city_cliffwood", "city_cliffwood beach", "city_clifton", "city_clinton", "city_clinton corners", "city_clinton township", "city_cohasset", "city_cold spring", "city_college point", "city_collingswood", "city_colonia", "city_colrain", "city_colts neck", "city_columbus", "city_concord", "city_congers", "city_cookstown", "city_copake", "city_copake falls", "city_coram", "city_corona", "city_cortlandt manor", "city_cotuit", "city_cranbury", "city_cranford", "city_craryville", "city_cream ridge", "city_croton on hudson", "city_crown point", "city_cummaquid", "city_dalton", "city_danvers", "city_dartmouth", "city_dedham", "city_deerfield", "city_del haven", "city_delanco", "city_delaware", "city_delran", "city_dennis", "city_dennis port", "city_dennisville", "city_denville", "city_deptford", "city_devens", "city_dighton", "city_dobbs ferry", "city_dorchester", "city_dorothy", "city_douglas", "city_douglaston", "city_dover", "city_dover plains", "city_dracut", "city_dresden", "city_dudley", "city_dumont", "city_dunellen", "city_dunstable", "city_duxbury", "city_east amwell", "city_east amwell township", "city_east boston", "city_east bridgewater", "city_east brunswick", "city_east chatham", "city_east dennis", "city_east elmhurst", "city_east falmouth", "city_east flatbush", "city_east greenbush", "city_east greenwich township", "city_east hanover", "city_east longmeadow", "city_east marion", "city_east nassau", "city_east orange", "city_east rutherford", "city_east sandwich", "city_east setauket", "city_east windsor", "city_eastampton", "city_eastchester", "city_eastham", "city_easthampton", "city_easton", "city_eatontown", "city_edgartown", "city_edgewater", "city_edgewater park", "city_edison", "city_egg harbor city", "city_egg harbor township", "city_egremont", "city_elberon", "city_eldred", "city_elizabeth", "city_elizabeth city", "city_elizabethtown", "city_elizaville", "city_elmer", "city_elmhurst", "city_elmont", "city_elmsford", "city_elmwood park", "city_emerson", "city_englishtown", "city_erial", "city_erma", "city_essex", "city_essex fells", "city_estell manor", "city_everett", "city_evesham", "city_ewing", "city_ewing township", "city_fair haven", "city_fair lawn", "city_fairfield", "city_fairfield twp", "city_fairhaven", "city_fall river", "city_falmouth", "city_fanwood", "city_far hills", "city_far rockaway", "city_farmingdale", "city_farmingville", "city_fitchburg", "city_flemington", "city_floral park", "city_florence", "city_florham park", "city_florida", "city_flushing", "city_fords", "city_forest hills", "city_forestdale", "city_forked river", "city_fort ann", "city_fort lee", "city_foxboro", "city_framingham", "city_frankford township", "city_franklin", "city_franklin lakes", "city_franklin park", "city_franklin twp", "city_franklinville", "city_fredon township", "city_freehold", "city_freetown", "city_frelinghuysen", "city_frenchtown", "city_fresh meadows", "city_gallatin", "city_galloway", "city_galloway township", "city_gardner", "city_garfield", "city_garnerville", "city_garwood", "city_georgetown", "city_ghent", "city_gibbsboro", "city_gibbstown", "city_gill", "city_glassboro", "city_glen cove", "city_glen gardner", "city_glen head", "city_glen ridge boro township", "city_glen rock", "city_glen spey", "city_glendale", "city_gloucester", "city_gloucester city", "city_grafton", "city_granby", "city_granville", "city_granville village", "city_great barrington", "city_great neck", "city_green brook", "city_green township", "city_greenfield", "city_greenport", "city_greenville", "city_greenwich", "city_greenwich township", "city_greenwood lake", "city_groton", "city_guttenberg", "city_hackettstown", "city_haddon heights", "city_haddon township", "city_haddonfield", "city_hadley", "city_hague", "city_hainesport", "city_haledon", "city_halifax", "city_hamburg", "city_hamilton", "city_hamilton township", "city_hammonton", "city_hampden", "city_hampton", "city_hancock", "city_hancocks bridge", "city_hanover", "city_hanover twp", "city_hanson", "city_harding township", "city_hardwick twp", "city_hardyston", "city_harriman", "city_harrison", "city_hartford", "city_hartsdale", "city_harvard", "city_harvey cedars", "city_harwich", "city_harwich port", "city_hasbrouck heights", "city_hastings on hudson", "city_haverhill", "city_haverstraw", "city_hawthorne", "city_hazlet", "city_hebron", "city_heislerville", "city_hempstead", "city_high bridge", "city_highland lake", "city_highland mills", "city_highland park", "city_highlands", "city_hightstown", "city_hillsborough", "city_hillsborough twp", "city_hillsdale", "city_hillside", "city_hingham", "city_hinsdale", "city_ho ho kus", "city_hoboken", "city_holbrook", "city_holden", "city_holland", "city_holland township", "city_hollis", "city_hollis hills", "city_holliston", "city_holmdel", "city_holmes", "city_holyoke", "city_hoosick falls", "city_hopatcong", "city_hopedale", "city_hopelawn", "city_hopewell", "city_hopewell junction", "city_hopewell township", "city_hopkinton", "city_howard beach", "city_howell", "city_hubbardston", "city_hudson", "city_hudson falls", "city_hull", "city_huntington", "city_hyannis", "city_independence township", "city_interlaken", "city_ipswich", "city_irvington", "city_iselin", "city_island heights", "city_jackson", "city_jackson heights", "city_jamaica", "city_jamaica plain", "city_jamesburg", "city_jefferson township", "city_jersey city", "city_jobstown", "city_juliustown", "city_kauneonga lake", "city_keansburg", "city_kearny", "city_keeseville", "city_kendall park", "city_kenilworth", "city_kew gardens", "city_keyport", "city_kinderhook", "city_kingsbury", "city_kingston", "city_kingwood", "city_kingwood township", "city_kinnelon", "city_knowlton", "city_lacey", "city_lagrangeville", "city_lake grove", "city_lakehurst", "city_lakeville", "city_lakewood", "city_lambertville", "city_lancaster", "city_landisville", "city_lanesborough", "city_lanoka harbor", "city_larchmont", "city_laurel springs", "city_laurelton", "city_lavallette", "city_lawnside", "city_lawrence", "city_lawrence township", "city_lawrenceville", "city_lebanon", "city_lee", "city_leicester", "city_lenox", "city_leominster", "city_leonardo", "city_lewis", "city_lexington", "city_liberty township", "city_lincoln", "city_lincoln park", "city_lincroft", "city_linden", "city_lindenwold", "city_linwood", "city_little egg harbor", "city_little egg harbor township", "city_little falls", "city_little ferry", "city_little neck", "city_little silver", "city_littleton", "city_livingston", "city_locust", "city_lodi", "city_long beach township", "city_long branch", "city_long hill township", "city_long island city", "city_longmeadow", "city_longport", "city_lopatcong", "city_lowell", "city_lower township", "city_ludlow", "city_lumberton", "city_lunenburg", "city_lyndhurst", "city_lynn", "city_lynnfield", "city_madison", "city_magnolia", "city_mahopac", "city_malden", "city_mamaroneck", "city_manahawkin", "city_manalapan", "city_manasquan", "city_manchester", "city_manchester township", "city_manhasset", "city_manhattan", "city_mansfield", "city_mantoloking", "city_mantua", "city_manville", "city_maple shade", "city_maplewood", "city_marblehead", "city_margate", "city_margate city", "city_marion", "city_marlboro", "city_marlborough", "city_marlton", "city_marmora", "city_marshfield", "city_marstons mills", "city_mashpee", "city_maspeth", "city_matawan", "city_mattapoisett", "city_mauricetown", "city_maynard", "city_mays landing", "city_medfield", "city_medford", "city_medford lakes", "city_medway", "city_melrose", "city_mendham", "city_mendham township", "city_mendon", "city_menlo park terrace", "city_merchantville", "city_merrimac", "city_methuen", "city_metuchen", "city_mickleton", "city_middle island", "city_middle village", "city_middleboro", "city_middlesex", "city_middleton", "city_middletown", "city_midland park", "city_milan", "city_milford", "city_millbrook", "city_millburn", "city_millbury", "city_miller place", "city_millerton", "city_millis", "city_millstone", "city_milltown", "city_millville", "city_milmay", "city_milton", "city_mine hill", "city_mizpah", "city_monmouth beach", "city_monmouth junction", "city_monroe", "city_monroe township", "city_monroeville", "city_monsey", "city_monson", "city_montague", "city_montauk", "city_montclair", "city_montebello", "city_monterey", "city_montgomery", "city_montgomery twp", "city_monticello", "city_montvale", "city_montville", "city_montville township", "city_monument beach", "city_moorestown", "city_morganville", "city_moriah", "city_morris plains", "city_morris twp", "city_morrisonville", "city_morristown", "city_mount arlington", "city_mount ephraim", "city_mount holly", "city_mount laurel", "city_mount olive township", "city_mount royal", "city_mount sinai", "city_mount vernon", "city_mountain lakes", "city_mountainside", "city_mountainville", "city_mullica", "city_mullica hill", "city_nahant", "city_nantucket", "city_nanuet", "city_narrowsburg", "city_nassau", "city_natick", "city_national park", "city_needham", "city_neponsit", "city_neptune city", "city_neptune township", "city_new ashford", "city_new bedford", "city_new braintree", "city_new brunswick", "city_new city", "city_new egypt", "city_new hyde park", "city_new lebanon", "city_new marlborough", "city_new monmouth", "city_new providence", "city_new rochelle", "city_new seabury", "city_new york", "city_new york city", "city_newark", "city_newbury", "city_newburyport", "city_newfield", "city_newport", "city_newton", "city_newtonville", "city_norfolk", "city_normandy beach", "city_north adams", "city_north andover", "city_north arlington", "city_north attleboro", "city_north bergen", "city_north brookfield", "city_north brunswick", "city_north brunswick township", "city_north caldwell", "city_north cape may", "city_north chatham", "city_north falmouth", "city_north greenbush", "city_north haledon", "city_north hills", "city_north middletown", "city_north plainfield", "city_north reading", "city_north salem", "city_north truro", "city_north wildwood", "city_north woodmere", "city_northampton", "city_northborough", "city_northbridge", "city_northeast", "city_northfield", "city_northvale", "city_norton", "city_norwell", "city_norwood", "city_nutley", "city_ny", "city_nyack", "city_oak bluffs", "city_oakham", "city_oakhurst", "city_oaklyn", "city_ocean city", "city_ocean gate", "city_ocean grove", "city_ocean township", "city_ocean view", "city_oceanport", "city_old bridge", "city_old bridge township", "city_old brookville", "city_old chatham", "city_old field", "city_old mill basin", "city_old tappan", "city_orange", "city_orangeburg", "city_orleans", "city_ortley beach", "city_ossining", "city_osterville", "city_otis", "city_oxford", "city_ozone park", "city_palisades", "city_palmer", "city_palmyra", "city_paramus", "city_park ridge", "city_parlin", "city_parsippany troy hills", "city_parsippany troy hills township", "city_passaic", "city_paterson", "city_patterson", "city_paulsboro", "city_pawling", "city_paxton", "city_peabody", "city_pearl river", "city_pedricktown", "city_peekskill", "city_pelham", "city_pemberton", "city_pembroke", "city_pennington", "city_penns grove", "city_pennsauken", "city_pennsville", "city_pepperell", "city_pequannock", "city_pequannock township", "city_perrineville", "city_perth amboy", "city_peru", "city_petersburgh", "city_phillipsburg", "city_phillipston", "city_philmont", "city_piermont", "city_pilesgrove", "city_pine beach", "city_pine plains", "city_piscataway", "city_piscataway twp", "city_pitman", "city_pittsfield", "city_pittsgrove", "city_pittstown", "city_plainfield", "city_plainsboro", "city_plainville", "city_plattsburgh", "city_pleasantville", "city_plumsted", "city_plymouth", "city_plympton", "city_pocasset", "city_poestenkill", "city_pohatcong township", "city_point pleasant", "city_point pleasant beach", "city_pomona", "city_pompton lakes", "city_pond eddy", "city_port jefferson", "city_port jefferson station", "city_port jervis", "city_port monmouth", "city_port norris", "city_port republic", "city_port washington", "city_poughkeepsie", "city_poughquag", "city_pound ridge", "city_princeton", "city_princeton junction", "city_prosp leff gdns", "city_prospect park", "city_provincetown", "city_purchase", "city_putnam valley", "city_queens", "city_queens village", "city_quincy", "city_rahway", "city_ramsey", "city_randolph", "city_raritan", "city_raynham", "city_reading", "city_readington", "city_readington twp", "city_red bank", "city_red hook", "city_rego park", "city_rehoboth", "city_revere", "city_richland", "city_richmond", "city_richmond hill", "city_richmond hill south", "city_ridge", "city_ridgefield park village", "city_ridgewood", "city_ridgewood village", "city_ringoes", "city_ringwood", "city_rio grande", "city_river edge", "city_river vale", "city_riverside", "city_riverton", "city_robbinsville", "city_rochester", "city_rockaway", "city_rockaway boro", "city_rockaway park", "city_rockland", "city_rockport", "city_rocky hill", "city_rocky point", "city_roebling", "city_roosevelt", "city_rosedale", "city_roseland", "city_roselle", "city_roslindale", "city_roslyn", "city_roslyn heights", "city_rouses point", "city_rowley", "city_roxbury township", "city_royalston", "city_rumson", "city_runnemede", "city_russell", "city_rutherford", "city_rutland", "city_rye", "city_rye brook", "city_saddle brook", "city_sagamore beach", "city_saint albans", "city_salem", "city_salisbury", "city_salisbury mills", "city_salt point", "city_sand lake", "city_sandisfield", "city_sands point", "city_sandwich", "city_sandyston", "city_saugus", "city_savoy", "city_sayreville", "city_scarborough", "city_scarsdale", "city_schodack landing", "city_schuyler falls", "city_scituate", "city_scotch plains", "city_sea bright", "city_sea cliff", "city_sea girt", "city_sea isle city", "city_seaside heights", "city_seaside park", "city_seaville", "city_secaucus", "city_seekonk", "city_selden", "city_setauket", "city_sewell", "city_shamong", "city_sharon", "city_sheffield", "city_sherborn", "city_shiloh", "city_ship bottom", "city_shirley", "city_shoreham", "city_shrewsbury", "city_shutesbury", "city_sicklerville", "city_skillman", "city_sleepy hollow", "city_sloatsburg", "city_smallwood", "city_smithville", "city_somerdale", "city_somers", "city_somers point", "city_somerset", "city_somerville", "city_sound beach", "city_south amboy", "city_south bound brook", "city_south brunswick", "city_south chatham", "city_south dennis", "city_south end", "city_south hadley", "city_south harrison township", "city_south orange village", "city_south orange village township", "city_south ozone park", "city_south plainfield", "city_south river", "city_south salem", "city_south setauket", "city_south yarmouth", "city_southampton", "city_southborough", "city_southbridge", "city_southold", "city_southwick", "city_sparrow bush", "city_sparta", "city_spencer", "city_spencertown", "city_spotswood", "city_spring lake", "city_spring lake heights", "city_spring valley", "city_springfield", "city_springfield gardens", "city_staatsburg", "city_stafford township", "city_stanfordville", "city_stanhope", "city_staten island", "city_stephentown", "city_sterling", "city_stewartsville", "city_stillwater", "city_stockbridge", "city_stockton", "city_stone harbor", "city_stoneham", "city_stony brook", "city_stony point", "city_stormville", "city_stoughton", "city_stow", "city_stratford", "city_strathmere", "city_sturbridge", "city_stuyvesant", "city_stuyvesant hts", "city_sudbury", "city_suffern", "city_sugar loaf", "city_summit", "city_sunderland", "city_surf city", "city_sussex", "city_sutton", "city_swainton", "city_swampscott", "city_swan lake", "city_swansea", "city_swedesboro", "city_sweetwater", "city_tabernacle", "city_taghkanic", "city_tallman", "city_tappan", "city_tarrytown", "city_taunton", "city_templeton", "city_tewksbury", "city_tewksbury township", "city_thiells", "city_thornwood", "city_thorofare", "city_ticonderoga", "city_tinton falls", "city_titusville", "city_tomkins cove", "city_toms river", "city_topsfield", "city_totowa", "city_totowa boro", "city_townbank", "city_townsend", "city_trenton", "city_truro", "city_tuckahoe", "city_tuckerton", "city_turnersville", "city_tuxedo park", "city_tyngsborough", "city_union beach", "city_union city", "city_union twp", "city_upper freehold", "city_upton", "city_uxbridge", "city_valatie", "city_valhalla", "city_valley cottage", "city_valley falls", "city_valley stream", "city_ventnor", "city_ventnor city", "city_ventnor heights", "city_verbank", "city_vernon", "city_verplanck", "city_villas", "city_vincentown", "city_vineland", "city_vineyard haven", "city_voorhees", "city_wading river", "city_wakefield", "city_wall", "city_wall township", "city_wallington", "city_walpole", "city_waltham", "city_wantage township", "city_ware", "city_wareham", "city_waretown", "city_warren", "city_warren twp", "city_warwick", "city_washington", "city_washington township", "city_washingtonville", "city_wassaic", "city_watchung", "city_waterford works", "city_watertown", "city_wayland", "city_wayne", "city_webster", "city_weehawken", "city_wellesley", "city_wellfleet", "city_wenham", "city_wenonah", "city_west allenhurst", "city_west amwell", "city_west atlantic city", "city_west barnstable", "city_west berlin", "city_west boylston", "city_west bridgewater", "city_west brookfield", "city_west caldwell", "city_west cape may", "city_west chazy", "city_west collingswood", "city_west creek", "city_west dennis", "city_west deptford", "city_west falmouth", "city_west harrison", "city_west harwich", "city_west haverstraw", "city_west long branch", "city_west milford", "city_west newbury", "city_west nyack", "city_west orange", "city_west springfield", "city_west stockbridge", "city_west tisbury", "city_west wareham", "city_west wildwood", "city_west windsor", "city_west yarmouth", "city_westampton", "city_westborough", "city_westfield", "city_westford", "city_westminster", "city_westmont", "city_weston", "city_westport", "city_westtown", "city_westville", "city_westwood", "city_weymouth", "city_wharton", "city_white creek", "city_white lake", "city_white plains", "city_white township", "city_whitehall", "city_whitehall village", "city_whitestone", "city_whiting", "city_whitman", "city_wilbraham", "city_wildwood", "city_wildwood crest", "city_williamsburg", "city_williamstown", "city_willingboro", "city_williston park", "city_willsboro", "city_wilmington", "city_winchendon", "city_winchester", "city_windsor", "city_wingdale", "city_winthrop", "city_woburn", "city_woodbine", "city_woodbridge", "city_woodbridge proper", "city_woodbury", "city_woodbury heights", "city_woodhaven", "city_woodland park", "city_woods hole", "city_woodside", "city_woodstown", "city_woolwich township", "city_worcester", "city_worthington", "city_wrentham", "city_wrightstown", "city_wyckoff", "city_yarmouth", "city_yarmouth port", "city_yonkers", "state_massachusetts", "state_new jersey", "state_new york"]
with open("model.joblib", 'rb') as file:
    models = joblib.load(file)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def model():
    data = request.get_json()
    city = data.get('city')
    loc_index = X.index(city) if city in X else -1

    x = np.zeros(len(X))
    x[0] = int(data.get('bedrooms'))
    x[1] = int(data.get('bathrooms'))
    x[2] = float(data.get('squareMeters'))
    if loc_index >= 0:
        x[loc_index] = 1


    prediction = models.predict([x])

    response_data = {'prediction': prediction[0]}
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True)