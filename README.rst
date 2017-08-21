*********************
collective.statusview
*********************

Overview
========



This Plone add-on provides a configurable status view.

The view  is similar to the standard ``@@ok``, used in `status checking`__, but is configurable.

__ https://docs.plone.org/manage/deploying/production/status_check.html

The user can configure if the site is considered "healthy" or "sick", and the view will return the
corresponding HTTP status code and body text. The configuration can be done per Zope instance or
globally.

The goal is to have a mechanism to remove/include Zope instances in a cluster, without setting
the status of the instances directly in the front end server (eg. Varnish).


Basic Usage
===========

The view is called ``@@status``.

Configuration is done in the ``Status View`` configlet in the Plone control panel. The following
settings are available:

Global status
	Healthy, sick or per-instance?
Current instance status
	Healthy or sick? Global status must be set to "per-instance" for this to take effect.
Healthy status
	The HTTP status code to return when the instance is healthy. Default: 200.
Sick status
	The HTTP status code to return when the instance is sick. Default: 500.
Healthy text
	The text to return when the instance is healthy. Default: healthy.
Sick text
	The text to return when the instance is sick. Default: sick.


Global Status vs Instance Status
================================

The global status can be "healthy", "sick" or "per-instance". The instance status can be
"healthy" or "sick".

The view will return "healthy" or "sick" according to the following algorithm:

.. code-block: python

   if global_status != 'per-instance':
       return global_status
   else:
       return instance_status

The global status is stored in ZODB. The instance status is stored in memory. When the instance
is started it is set to "healthy".

Changing the global status value _never_ changes the instance status and vice-versa. They are
completely independent.

Example:




+----------------------------------------------+---------------+-----------------+--------------+
| Action                                       | Global Status | Instance status | View returns |
+==============================================+===============+=================+==============+
| Zope instance starts and add-on is installed | HEALTHY       | HEALTHY         | *HEALTHY*    |
+----------------------------------------------+---------------+-----------------+--------------+
| User set instance status to SICK             | HEALTHY       | SICK            | *HEALTHY*    |
+----------------------------------------------+---------------+-----------------+--------------+
| User set global status to SICK               | SICK          | SICK            | *SICK*       |
+----------------------------------------------+---------------+-----------------+--------------+
| User set global status to HEALTHY            | HEALTHY       | SICK            | *HEALTHY*    |
+----------------------------------------------+---------------+-----------------+--------------+
| User set global status to PER-INSTANCE       | PER-INSTANCE  | SICK            | *SICK*       |
+----------------------------------------------+---------------+-----------------+--------------+



Web API
=======

The ``@@manage-status-view`` allows to get/set the status.

The view accepts the following HTTP methods:

``GET``
	Get the status. A JSON object will be returned, containg the global status, the instance
	status and the status that ``@@status`` will actually return.
``POST``
	Set the status. Parameters:

	``global``
		Value must be one of: ``healthy``, ``sick`` or ``per-instance``.
	``instance``
		Value must be one of: ``healthy`` or ``sick``.

	The same body returned for the ``GET`` method is returned, allowing to inspect what is the
	new status.
