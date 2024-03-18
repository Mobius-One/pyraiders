## Remembering things is hard and I'm sure this will get done in no time. Amirite.

### Priority
* Fix stuck placement loop which will most likely fix the idler switcher.
    * Improve placement precision.
    * Improve raid state handler to cover additional uncaught issues (INVALID_RAID_STATE:9 and some others).
* Fix idler switcher triggering when it's not supposed to.
    * Fix masterlist/any_captain switch behaviour on startup. Runtime works fine!?
    * Fix masterlist not hot switching properly when any_captain is disabled
* Protect slots against captains switching modes.
* Log 5 loyalty switch is broken

### Not priority
* Figure out the epic unit placement offsetting.
* Auto shop dealing.
* Unit auto level up system.
* Fix or scrap slot counter because it doesn't work as expected.
* Support for pvp.
* Force swap captains based on the block list.