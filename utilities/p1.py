"""
    Find some interesting information in flight vectors
    ...
"""
import math
import json


def haversine(lat1, lon1, lat2, lon2):
    """
    Haversine Formula - Distance between two GPS points)
    :param lat1: latitude of the 1st point
    :param lon1: longitude of the 2nd point
    :param lat2: latitudes of the 2nd point
    :param lon2: longitude of the 2nd point
    :return: distance between latitudes and longitudes in kilometers
    """
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
         math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c


def highest_plane(vertical_rate):
    """
    Finds the highest flying plane based on the 'geo_altitude'
    :param vectors: list of dictionaries (flight vectors of planes)
    :return: dictionary containing the largest 'geo_altitude
    """
    pass


def lowest_plane(vectors):
    pass


def fastest_climber(vectors):
    pass


def fastest_descender(vectors):
    pass


def closest_to_ERAU(vectors):
    """
    Finds the plane closest to the ERAU campus in Prescott
    :param vectors: list of dictionaries (flight vectors of planes)
    :return: a tuple containing the closest plane and the distance to ERAU
    """
    # ERAU_Latitude = ...
    # ERAU_Longitude = ...
    # closest_plane = ..
    # distance = ..
    # return closest_plane, round(distance)


def closest_planes(vectors):
    """
    Finds the lowest flying plane based on the 'geo_altitude'
    :param vectors: list of dictionaries (flight vectors of planes)
    :return: a tuple containing the two airplanes closest to each other and their distance
    """
    # plane_1 ..
    # plane_2 ..
    # ..
    # ..
    # distance = ..
    # return plane_1, plane_1, round(distance)
