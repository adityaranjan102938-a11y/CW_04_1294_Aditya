#include <stdio.h>

#define max 30

int main()
{
    int i, n;
    int at[max], wt[max], bt[max], tat[max];
    int priority[max];
    int rem[max], ct[max];

    int completed = 0, time = 0;
    int priorityIndex, highestPriority;

    float awt = 0, atat = 0;

    printf("ENTER THE NUMBER OF PROCESSES: ");
    scanf("%d", &n);

    if (n <= 0 || n > max)
    {
        printf("Invalid number of processes.\n");
        return 1;
    }

    printf("ENTER THE BURST TIME OF PROCESSES:\n");

    for (i = 0; i < n; i++)
    {
        scanf("%d", &bt[i]);

        if (bt[i] <= 0)
        {
            printf("Burst time must be greater than zero.\n");
            return 1;
        }

        rem[i] = bt[i];
    }

    printf("ENTER THE ARRIVAL TIME OF PROCESSES:\n");

    for (i = 0; i < n; i++)
    {
        scanf("%d", &at[i]);

        if (at[i] < 0)
        {
            printf("Arrival time cannot be negative.\n");
            return 1;
        }
    }

    printf("ENTER THE PRIORITY OF PROCESSES:\n");
    printf("(Lower number means higher priority)\n");

    for (i = 0; i < n; i++)
    {
        scanf("%d", &priority[i]);

        if (priority[i] < 0)
        {
            printf("Priority cannot be negative.\n");
            return 1;
        }
    }

    while (completed < n)
    {
        priorityIndex = -1;
        highestPriority = 999999;

        /* students understand-dont write in file
         * Select the arrived process with the highest priority.
         * Lower priority number means higher priority.
         */
        for (i = 0; i < n; i++)
        {
            if (at[i] <= time &&
                rem[i] > 0 &&
                priority[i] < highestPriority)
            {
                highestPriority = priority[i];
                priorityIndex = i;
            }
        }

        /* students understand this-dont write in file
         * If no process has arrived, increase the CPU time.
         */
        if (priorityIndex == -1)
        {
            time++;
        }
        else
        {
            /* students kindly understand this-dont write in file
             * Execute the selected process for one unit of time.
             * The process can be preempted when a higher-priority
             * process arrives.
             */
            rem[priorityIndex]--;
            time++;

            if (rem[priorityIndex] == 0)
            {
                ct[priorityIndex] = time;
                completed++;
            }
        }
    }

    for (i = 0; i < n; i++)
    {
        tat[i] = ct[i] - at[i];
        wt[i] = tat[i] - bt[i];

        awt = awt + wt[i];
        atat = atat + tat[i];
    }

    printf("\nProcess\tBurst Time\tArrival Time\tPriority\tWaiting Time\tTurn Around Time\n");

    for (i = 0; i < n; i++)
    {
        printf("%d\t%d\t\t%d\t\t%d\t\t%d\t\t%d\n",
               i + 1,
               bt[i],
               at[i],
               priority[i],
               wt[i],
               tat[i]);
    }

    awt = awt / n;
    atat = atat / n;

    printf("\nAverage Waiting Time = %.2f\n", awt);
    printf("Average Turn Around Time = %.2f\n", atat);

    return 0;
}
