def llegada():
    """Descripción de la función.

    El parámetro :math:`\lambda` es de la distribución exponencial:

    .. math:: f_X(x) = \lambda e^{-\lambda x}

    Parameters
    ----------
    x : int
        Descripción del parámetro.
    y : string
        Descripción del parámetro.

    Returns
    -------
    z : float
        Descripción de la respuesta.

    Examples
    --------
    >>> cadena.analisis.llegada(clientes)
    lambda = 0.25
    """
    return 'Función llegada().'

def servicio():
    """Descripción de la función.

    Parameters
    ----------
    x : int
        Descripción del parámetro.
    y : string
        Descripción del parámetro.

    Returns
    -------
    z : float
        Descripción de la respuesta.
    """
    return 'Función servicio().'

def parametros():
    """Descripción de la función.

    Parameters
    ----------
    x : int
        Descripción del parámetro.
    y : string
        Descripción del parámetro.

    Returns
    -------
    z : float
        Descripción de la respuesta.
    
    Examples
    --------
    >>> cadena.analisis.parametros(lambd, nu)
    omega_i = 0.2 + 0.019*i
    p_i = 0.2 / (0.2 + 0.019*i)
    q_i = 0.019*i / (0.2 + 0.019*i)

    Valor numérico para un estado i específico:

    >>> cadena.analisis.parametros(lambd, nu, i)
    omega = 0.36
    p = 0.3
    q = 0.7
    """
    return 'Función parametros().'