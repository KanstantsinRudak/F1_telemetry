import fastf1 as ff1

ff1.Cache.enable_cache('cache')

def get_f1_laps_df(drivers, year, grand_prix, session):
    quali = ff1.get_session(year, grand_prix, session)
    quali.load()
    laps_df = quali.laps.pick_drivers(drivers)
    return laps_df

def get_f1_telemetry_df(drivers, year, grand_prix, session):
    quali = ff1.get_session(year, grand_prix, session)
    quali.load()
    laps_df = quali.laps.pick_drivers(drivers)
    fastest_df = laps_df.pick_fastest()
    telemetry_driver_1 = fastest_df.get_telemetry().add_distance().add_track_status()
    return telemetry_driver_1

def get_f1_session_data(year, grand_prix, session):
    session = ff1.get_session(year, grand_prix, session)
    session.load(telemetry=False, weather=False)
    session_df = session.laps
    return session_df




