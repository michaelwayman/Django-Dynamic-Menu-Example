$(document).ready ->
  animationFinished = false
  $nav = $(".nav")
  $navBtn = $(".nav-btn")
  $activates = $(".nav, .nav-btn, .nav-item-menu, .nav-item-submenu")
  $navBtn.on 'mouseenter', ->
    if not $nav.hasClass 'active'
      $activates.addClass 'active'

  $("#nav").on 'mouseleave', ->
    if animationFinished
      $activates.removeClass 'active'

  $nav.on 'oTransitionEnd msTransitionEnd transitionend webkitTransitionEnd', ->
    if $nav.hasClass 'active'
      animationFinished = true
    else
      animationFinished = false
