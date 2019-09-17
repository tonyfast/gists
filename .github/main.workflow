workflow "on push" {
  on = "push"
  resolves = ["GitHub Action for pytest"]
}

action "GitHub Action for pytest" {
  uses = "tonyfast/gists@master"
  args = "pytest"
}
