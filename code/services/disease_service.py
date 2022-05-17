from fastapi import APIRouter, HTTPException
from fastapi.exceptions import RequestValidationError

from managers.utils import transform_params
from repositories.ccaa_repository import CcaaRepository
from repositories.cie_repository import CieRepository
from repositories.disease_reopsitory import DiseaseRepository
from repositories.gedad_repository import GedadRepository
from repositories.raziel_repository import RazielRepository
from repositories.vars_repository import VarsRepository

router = APIRouter(
    responses={404: {"description": "Not found"}}
)

@router.get("/diseases", status_code=200)
def get_diseases(sort: str = None, query: str = None, page: int = None, limit: int = None):
    """
    Get all disease atendiendo al siguiente orden
    - `sort` propiedad por la que ordenar `'-propiedad'` sentido descendiente
    - `query` formato de la query: `{'defu': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = DiseaseRepository('data/diseases', CieRepository('data/cie'))
    try:
        p = transform_params(sort, query, page, limit)
        objs, tam = c.get_all(p)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {
        'items': objs,
        'length': tam
    }


@router.get("/ccaas")
def get_ccaas(sort: str = None, query: str = None, page: int = None, limit: int = None):
    """
    Get all disease atendiendo al siguiente orden
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = CcaaRepository('data/ccaas')
    objs, tam = c.get_all(transform_params(sort, query, page, limit))
    return {
        'items': objs,
        'length': tam
    }


@router.get("/cie")
def get_cies(sort: str = None, query: str = None, page: int = None, limit: int = None):
    """
    Get all CIE diseases clasification.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = CieRepository('data/cie')
    objs, tam = c.get_all(transform_params(sort, query, page, limit))
    return {
        'items': objs,
        'length': tam
    }


@router.get("/cie")
def get_cies(sort: str = None, query: str = None, page: int = 1, limit: int = 100):
    """
    Get all CIE diseases clasification.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = CieRepository('data/cie')
    objs, tam = c.get_all(transform_params(sort, query, page, limit))
    return {
        'items': objs,
        'length': tam
    }


@router.get("/ages-groups")
def get_ages_groups(sort: str = None, query: str = None, page: int = None, limit: int = None):
    """
    Grupos de edad disponibles para clasificar.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = GedadRepository('data/grupos_edad')
    objs, tam = c.get_all(transform_params(sort, query, page, limit))
    return {
        'items': objs,
        'length': tam
    }


@router.get("/raziel")
def get_raziel_diseases(sort: str = None, query: str = None, page: int = 1, limit: int = 100):
    """
    Grupos de edad disponibles para clasificar.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = RazielRepository(
        'data/raziel',
        DiseaseRepository('data/diseases', CieRepository('data/cie')),
        CcaaRepository('data/ccaas'),
        GedadRepository('data/grupos_edad')
    )
    p = transform_params(sort, query, page, limit)
    objs, tam = c.get_all(p)
    return {
        'items': objs,
        'length': tam
    }


@router.get("/vars-meaning")
def get_vars_meaning():
    c = VarsRepository('data/vars')
    objs, tam = c.get_all()
    return {
        'items': objs,
        'length': tam
    }
