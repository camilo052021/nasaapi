-----/*esta es una vista de referecnia para ejecutar en el pg admin*/--------
CREATE VIEW relex as
SELECT * FROM public.results
WHERE id_y is not null;