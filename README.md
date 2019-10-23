Building a Meetup Clone
------------------
A client comes to you looking to build a new business. Well, mainly it's a clone of the site
Meetup.com. At its heart, it's just a CRUD like everything else, but there are
a lot of particularities that make the site interesting.

The basic idea is this: Users can register and create a group for people like
themselves based on their common interests. Linux Administrators, Dog Owners,
Redhead Trapeze Artists. Anything your heart desires.

Once a user creates a group, other users can join those groups and group members can
create events relevant to the group.

Release 0: Auth
------------------
Use django's default library to handle creation and authentication of users.

Release 1: Generate Models
------------------
Let's create our models. Here are the entities we're going to create
models and migrations for:
* User
  * A user should be able to access his/her groups and only a group's owner can make edits to the group
* Group
  * Attributes can include: title, owner, description, etc.
* Event
  * Attributes can include: group, date, title, description, image_url (if they want an image on their event)

Make sure to model the relationships between entities. For now it's OK if users can't RSVP for events,
we can save that for later.

Release 2: CRUD Groups
------------------
Add a link or button in the base template of the app to view the groups that exist (all groups,
regardless of the owner). Develop
the CRUD interface for groups that includes the ability to create and
manipulate groups.

Only the owner of a group should be able edit or destroy the group.

Release 3: Group Events
------------------
When viewing a group, display a list of upcoming and previous events for that
group. The owner of a group should be able to add, edit and delete events for
the group.

If the user provides a URL to an image, make sure to display that image in the
list of events. Studies show people trust websites with lots of photos more
than websites without photos.

On the event show page, show the description of the event itself and link back
to the group.

Release 4: Add the Homepage
------------------
At the root route of the app, show me a list of ten upcoming events. You can 
re-use the template you created for the group show page, but also show a link to 
the group itself for each event, so that I can go look at the group associated 
with the event.

Release 5: Add a Tutorial Page
------------------
Add a boolean flag to the user model to check whether they've seen the
"tutorial" page yet. Whenever a user tries to visit a page (other than the
signup pages), check for that flag. If they haven't seen the tutorial yet,
redirect them to a simple tutorial page.

For now, it's okay to just put some nonsense content into that tutorial page.
Make sure to reset the flag on the user model so that the user isn't
perpetually redirected back to this page.

Release 6: Members of Groups
------------------
If I am a user that visits a group, let me click a button to "join" that group.
Change the group page to display all members of a group, and on what date they
joined. If I'm already a member, let me leave the group instead if I click a
button.

The owner of a group should always be a member of that group.

Question: How should these view functions be structured? Is this a CRUD of
its own? If so, of what entity is it a CRUD? Spend some time thinking before
you implement the functionality for this path; these kinds of ancillary
interfaces often become the most confusing and fun parts of an app.
