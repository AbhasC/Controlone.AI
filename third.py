import csv


class WarehouseParcelDetail:
    def __init__(self, parcel_number, parcel_weight, parcel_category):
        self.parcel_number = parcel_number
        self.parcel_weight = parcel_weight
        self.parcel_category = parcel_category

    def save_and_display_parcel_details(self, parcels):
        with open("parcel_details.csv", "w", newline="") as csvfile:
            fieldnames = ["Parcel Number", "Parcel Weight", "Parcel Category"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for parcel in parcels:
                writer.writerow(
                    {
                        "Parcel Number": parcel.parcel_number,
                        "Parcel Weight": parcel.parcel_weight,
                        "Parcel Category": parcel.parcel_category,
                    }
                )

        filters = [
            parcel.parcel_number
            for parcel in parcels
            if parcel.parcel_category == "filters"
        ]
        automobile_parts = [
            parcel.parcel_number
            for parcel in parcels
            if parcel.parcel_category == "automobile_parts"
        ]
        cargo_containers = [
            parcel.parcel_number
            for parcel in parcels
            if parcel.parcel_category == "cargo_container"
        ]

        print("Filters\t\tautomobile_parts\t\tcargo_container")
        for i in range(
            max(
                len(filters),
                len(automobile_parts),
                len(cargo_containers),
            )
        ):
            filter_number = filters[i] if i < len(filters) else ""
            automobile_parts_number = (
                automobile_parts[i] if i < len(automobile_parts) else ""
            )
            cargo_container_number = (
                cargo_containers[i] if i < len(cargo_containers) else ""
            )
            print(
                f" {filter_number}\t\t\t{automobile_parts_number}\t\t\t{cargo_container_number}"
            )


parcel_detail = {
    WarehouseParcelDetail("23456", 5.0, "filters"),
    WarehouseParcelDetail("66234", 10.0, "automobile_parts"),
    WarehouseParcelDetail("98432", 15.0, "cargo_container"),
    WarehouseParcelDetail("96355", 6.0, "filters"),
    WarehouseParcelDetail("86643", 12.0, "automobile_parts"),
    WarehouseParcelDetail("53463", 18.0, "cargo_container"),
    WarehouseParcelDetail("83722", 7.0, "filters"),
    WarehouseParcelDetail("64326", 14.0, "automobile_parts"),
    WarehouseParcelDetail("87653", 20.0, "cargo_container"),
}

warehouse = WarehouseParcelDetail(None, None, None)
warehouse.save_and_display_parcel_details(parcel_detail)
