import os
from typing import Optional

# from pydantic import BaseModel, Field
from serpapi import GoogleSearch
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import tool
from dotenv import load_dotenv

_=load_dotenv()
class FlightsInput(BaseModel):
    departure_airport: Optional[str] = Field(description='Departure airport code (IATA)')
    arrival_airport: Optional[str] = Field(description='Arrival airport code (IATA)')
    outbound_date: Optional[str] = Field(description='Parameter defines the outbound date. The format is YYYY-MM-DD. e.g. 2024-06-22')
    return_date: Optional[str] = Field(description='Parameter defines the return date. The format is YYYY-MM-DD. e.g. 2024-06-28')
    adults: Optional[int] = Field(1, description='Parameter defines the number of adults. Default to 1.')
    children: Optional[int] = Field(0, description='Parameter defines the number of children. Default to 0.')
    infants_in_seat: Optional[int] = Field(0, description='Parameter defines the number of infants in seat. Default to 0.')
    infants_on_lap: Optional[int] = Field(0, description='Parameter defines the number of infants on lap. Default to 0.')

class FlightsInputSchema(BaseModel):
    params: FlightsInput

@tool(args_schema=FlightsInputSchema)
def flights_finder(params: FlightsInput):
    '''
    Find flights using the Google Flights engine.
    
    Returns:
        dict: Flight search results.
    '''
    
    search_params = {
        'api_key': os.environ.get('SERPAPI_API_KEY'),
        'engine': 'google_flights',
        'hl': 'en',
        'gl': 'us',
        'departure_id': params.departure_airport,
        'arrival_id': params.arrival_airport,
        'outbound_date': params.outbound_date,
        'return_date': params.return_date,
        'currency': 'USD',
        'adults': params.adults,
        'infants_in_seat': params.infants_in_seat,
        'stops': '1',
        'infants_on_lap': params.infants_on_lap,
        'children': params.children
    }
    
    try:
        search = GoogleSearch(search_params)
        results = search.get_dict()
        return results
    except Exception as e:
        return {"error": str(e)}

# Alternative version with corrected field names if the API expects different parameter names
class FlightsInputCorrected(BaseModel):
    departure_id: Optional[str] = Field(description='Departure airport code (IATA)')
    arrival_id: Optional[str] = Field(description='Arrival airport code (IATA)')
    outbound_date: Optional[str] = Field(description='Parameter defines the outbound date. The format is YYYY-MM-DD. e.g. 2024-06-22')
    return_date: Optional[str] = Field(description='Parameter defines the return date. The format is YYYY-MM-DD. e.g. 2024-06-28')
    adults: Optional[int] = Field(1, description='Parameter defines the number of adults. Default to 1.')
    children: Optional[int] = Field(0, description='Parameter defines the number of children. Default to 0.')
    infants_in_seat: Optional[int] = Field(0, description='Parameter defines the number of infants in seat. Default to 0.')
    infants_on_lap: Optional[int] = Field(0, description='Parameter defines the number of infants on lap. Default to 0.')

class FlightsInputCorrectedSchema(BaseModel):
    params: FlightsInputCorrected

@tool(args_schema=FlightsInputCorrectedSchema)
def flights_finder_corrected(params: FlightsInputCorrected):
    '''
    Find flights using the Google Flights engine (with corrected parameter names).
    
    Returns:
        dict: Flight search results.
    '''
    
    search_params = {
        'api_key': os.environ.get('SERPAPI_API_KEY'),
        'engine': 'google_flights',
        'hl': 'en',
        'gl': 'us',
        'departure_id': params.departure_id,
        'arrival_id': params.arrival_id,
        'outbound_date': params.outbound_date,
        'return_date': params.return_date,
        'currency': 'USD',
        'adults': params.adults,
        'infants_in_seat': params.infants_in_seat,
        'stops': '1',
        'infants_on_lap': params.infants_on_lap,
        'children': params.children
    }
    
    try:
        search = GoogleSearch(search_params)
        results = search.get_dict()
        return results
    except Exception as e:
        return {"error": str(e)}