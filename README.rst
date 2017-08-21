*********************
collective.statusview
*********************

Overview
========

This Plone add-on provides a configurable status view.

The view  is similar to the standard ``@@ok``, used in `status checking`__, but is configurable.

__ https://docs.plone.org/manage/deploying/production/status_check.html

The user can configure if the site is considered *healthy* or *sick*, and the view will return the
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

Healthy status
	The HTTP status code to return when healthy. Default: 200.

Sick status
	The HTTP status code to return when sick. Default: 500.

Healthy text
	The text to return when healthy. Default: healthy.

Sick text
	The text to return when sick. Default: sick.


.. IMPORTANT::

   Currently it is not possible to change the instance status using the control panel UI
   (it's in the TODO list). The `Web API`_ can be used for this.


Global Status vs Instance Status
================================

The global status can be *healthy*, *sick* or *per-instance*. The instance status can be *healthy*
or *sick*.

The ``@@status`` view will return *healthy* or *sick* according to the following algorithm:

.. code-block:: python

   if global_status != 'per-instance':
       return global_status
   else:
       return instance_status

The global status is stored in ZODB. The instance status is stored in memory. When the instance
is started it is set to *healthy*.

Changing the global status *never* changes the instance status, and vice-versa. They are
completely independent in this regard.

Example:

.. csv-table::
   :header: "Action", "Global Status", "Instance Status", "View Returns"

    Zope instance starts and add-on is installed, *healthy*,      *healthy*,  *healthy*
    Set instance status to sick,                  *healthy*,      *sick*,     *healthy*
    Set global status to *sick*,                  *sick*,         *sick*,     *sick*
    Set global status to *healthy*,               *healthy*,      *sick*,     *healthy*
    Set global status to *per-instance*,          *per-instance*, *sick*,     *sick*
    Set global status to *healthy*,               *healthy*,      *sick*,     *healthy*


Web API
=======

The ``@@manage-status-view`` allows to get and set the status.

The view accepts the following HTTP methods:

``GET``
	Get the status. A JSON object will be returned, containg the global status, the instance
	status and the status that ``@@status`` will actually return.

``POST``
	Set the status. Query string parameters:

	``global``
		One of: ``healthy``, ``sick`` or ``per-instance``.

	``instance``
		One of: ``healthy`` or ``sick``.

	The same body returned for the ``GET`` method is returned, allowing to inspect what is the
	new status.
