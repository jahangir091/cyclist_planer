import csv

from utils import planned_table, truth_table

def get_rider_data(rider_no):
    with open('sample_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rier_ftps = []
        for row in csv_reader:
            rier_ftps.append(int(row[rider_no+1]))
    return rier_ftps


def get_start_index(data, l_bound, u_bound):
    index_counter = 0
    for d in data:
        if l_bound <= d <=u_bound:
            break
        index_counter += 1

    return index_counter


def check_plan(rider_data, plan):
    lower_ftp = plan[3]
    upper_ftp = plan[4]
    start_index = get_start_index(rider_data, lower_ftp, upper_ftp)

    target_index = start_index + int((plan[1]*60 + plan[2])/5)
    if target_index > len(rider_data):
        return False, 0, rider_data

    for current_index in range(start_index,target_index):
        if lower_ftp <= rider_data[current_index] <= upper_ftp:
            pass
        else:
            return False, 0, rider_data[current_index:]

    point = truth_table[str(plan[0])]
    return True, point, rider_data[target_index:]


def main():
    riders = [1,2,3]
    for rider in riders:
        rider_data = get_rider_data(rider)
        total_point_gain = 0
        plan_no = 1
        for plan in planned_table:
            success, point, rider_data = check_plan(rider_data, plan)
            if success:
                print('For rider-{0} plan {1} success'.format(rider, plan_no))
                total_point_gain += point
            else:
                print('For rider-{0} plan {1} unsuccess'.format(rider, plan_no))
            plan_no += 1
        print('Rider {0} total point {1}'.format(rider, total_point_gain))



if __name__ == '__main__':
    main()