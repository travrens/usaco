# flowers = 100
# input = "336 490 644 324 895 121 801 290 291 405 192 694 443 427 332 20 20 224 286 460 112 643 385 355 355 936 518 839 834 829 824 819 814 809 804 799 794 789 784 779 774 769 764 759 754 749 744 739 734 729 724 719 714 709 704 699 694 689 684 679 674 669 664 659 654 649 644 639 634 629 624 619 614 609 604 599 594 589 584 579 574 569 564 559 554 549 544 539 534 529 524 519 514 509 504 499 494 489 484 479".split()
# petals = list(map(int, input))
flowers = int(input())
petals = list(map(int, input().split()))
photos = 0

for i in range(flowers):
    petalseen = 0
    found = set()
    for j in range(i,flowers):
        petalseen += petals[j]
        found.add(petals[j])
        if (petalseen % (j - i + 1)) == 0:
            if petalseen / (j - i + 1) in found:
                photos += 1
print(photos)